
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc,html
from dash import Input,Output
import plotly.express as px

external_stylesheet=[
    {
        'href':"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
        'rel':"stylesheet",
        'integrity':"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
        'crossorigin':"anonymous",
    }
]

patints = pd.read_csv("state_wise_daily data file IHHPET.csv")
total=patints.shape[0]
active=patints[patints['Status']=="Confirmed"].shape[0]
recovered=patints[patints['Status']=="Recovered"].shape[0]
deaths=patints[patints['Status']=="Deceased"].shape[0]

options=[
    {'label':'All','value':'All'},
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'}
]

options1=[
    {'label':'All','value':'All'},
    {'label': 'Mask', 'value': 'Mask'},
    {'label': 'Sanitizer', 'value': 'Sanitizer'},
    {'label': 'Oxygen', 'value': 'Oxygen'}
]

options2=[
    {'label': 'Red Zone', 'value': 'Red Zone'},
    {'label': 'Blue Zone', 'value': 'Blue Zone'},
    {'label': 'Green Zone', 'value': 'Green Zone'},
    {'label': 'Orange Zone', 'value': 'Orange Zone'}


]
app= dash.Dash(__name__,external_stylesheets =external_stylesheet)
app.layout=html.Div([
    html.H1('Corona Virus Pandemic',style={'color':'#fff','text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases",className='text-light'),
                    html.H4(total,className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases", className='text-light'),
                    html.H4(active, className='text-light')
                ], className='card-body')
            ], className='card bg-info')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases", className='text-light'),
                    html.H4(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-warning')
        ],className='col-md-3'),
        html.Div([            html.Div([
                html.Div([
                    html.H3("Total Deaths",className='text-light'),
                    html.H4(deaths,className='text-light')
                ],className='card-body')
            ],className='card bg-success')],className='col-md-3'),
    ],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph',options= options1,value="All"),
                    dcc.Graph(id='graph')
                ],className='card-body')
            ],className='card bg-success')
        ],className='col-md-6'),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown',options=options2,value='Status'),
                    dcc.Graph(id='the_graph')

                ],className='card-body')
            ],className='card')
        ],className='col-md-6')
    ],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker',options=options,value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')
    ],className='row'),
],className='container')

@app.callback(Output('bar','figure'),[Input('picker','value')])

def update_graph(value):
    if value=='All':
        fig=go.Figure(data=[go.Bar(x=patints['State'],y=patints['Total'])])
        fig.update_layout(title="State Total Counts",plot_bgcolor='orange')
        return fig
    else:
        fig=go.Figure(data=[go.Bar(x=patints['State'],y=patints[value])])
        fig.update_layout(title = f"State {value} Cases",
                          plot_bgcolor="orange")
        return fig

@app.callback(Output('graph','figure'),[Input('plot-graph','value')])
def generate_graph(type):
    if type=="All":
        return {'data':[go.Scatter(x=patints['Status'],y=patints['Total'])],
            'layout':go.Layout(title="Commodities Total Counts",plot_bgcolor='pink')}
    if type == "Mask":
        return {'data': [go.Scatter(x=patints['Status'], y=patints['Mask'])],
                'layout': go.Layout(title="Commodities Total Counts", plot_bgcolor='pink')}
    if type == "Sanitizer":
        return {'data': [go.Scatter(x=patints['Status'], y=patints['Sanitizer'])],
                'layout': go.Layout(title="Commodities Total Counts", plot_bgcolor='pink')}
    if type == "Oxygen":
        return {'data': [go.Scatter(x=patints['Status'], y=patints['Oxygen'])],
                'layout': go.Layout(title="Commodities Total Counts", plot_bgcolor='pink')}

@app.callback(Output('the_graph','figure'),[Input('my_dropdown','value')])
def generate_graph(my_dropdown):
    piechart = px.pie(data_frame=patints,names='State',values=my_dropdown,hole=0.3)
    return (piechart)
if __name__=='__main__':
    app.run(debug=True)

