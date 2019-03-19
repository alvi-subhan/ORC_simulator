## Introducing callbacks

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from dash.dependencies import Input, Output, State
import pandas as pd

app = dash.Dash()

df=pd.read_csv('/home/subhan-alvi/Downloads/names.csv')

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501


app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Hello World',
                        className='nine columns'),
                html.Img(
                    src="http://test.fulcrumanalytics.com/wp-content/uploads/2015/10/Fulcrum-logo_840X144.png",
                    className='three columns',
                    style={
                        'height': '9%',
                        'width': '9%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 10,
                    },
                ),
                html.Div(children='''
                        Dash: A web application framework for Python.
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [   
            html.Div([

                html.Label('Select Refrigerant:'),
                dcc.Dropdown(
                    id='Year',
                    options=[{'label': i, 'value': i} for i in df.Year.unique()],
                    placeholder='Select Year',
                    multi=True,
                    value=['4th'],
                    ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
                ], className="row"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose City:'),
                        dcc.Checklist(
                                id = 'Cities',
                                options=[
                                    {'label': 'San Francisco', 'value': 'SF'},
                                    {'label': 'Montreal', 'value': 'MT'}
                                ],
                                values=['SF', 'MT'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='four columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph'
                )
                ], className= 'row'
                ),

                html.Div([
                dcc.Graph(
                    id='Amount'
                )
                    ], className='row'        
                ),

                html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 9, 8], 'type': 'line', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Graph 2'
                        }
                    }
                )
                ], className= 'row'
                )
            ]
        ) 
    
    ], className='ten columns offset-by-one')
)
@app.callback(
    dash.dependencies.Output('Amount', 'figure'),
    [dash.dependencies.Input('Year', 'value')])
def update_image_src(selector):
    data=[]
    if '4th' in selector:
        indx=df[df['Year']=='4th'].index.tolist()
        x=df.Name[indx].tolist()
        y=df.Amount[indx].tolist()
        data.append({'x': x, 'y': y, 'type': 'bar', 'name': 'Amount Paid'})

    if '2nd' in selector:
        indx=df[df['Year']=='2nd'].index.tolist()
        x=df.Name[indx].tolist()
        y=df.Amount[indx].tolist()
        data.append({'x': x, 'y': y, 'type': 'bar', 'name': 'Amount Paid'})

    if '1st' in selector:
        indx=df[df['Year']=='1st'].index.tolist()
        x=df.Name[indx].tolist()
        y=df.Amount[indx].tolist()
        data.append({'x': x, 'y': y, 'type': 'bar', 'name': 'Amount Paid'})
    
    figure={
        'data':data,
        'layout':{'title':'Graph'}
    }
    
    return figure


@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('Cities', 'values')])
def update_image_src(selector):
    data = []
    if 'SF' in selector:
        data.append({'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'})
    if 'MT' in selector:
        data.append({'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 1',
            'xaxis' : dict(
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('Cities', 'values')])
def update_image_src(selector):
    data = []
    if 'SF' in selector:
        data.append({'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'})
    if 'MT' in selector:
        data.append({'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 2',
            'xaxis' : dict(
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure


if __name__ == '__main__':
    app.run_server(port=8050)