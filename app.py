import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Carrega os dados
df = pd.read_csv('ecommerce_estatistica.csv')

# Identifica automaticamente as colunas numéricas e categóricas
colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
col_y = colunas_numericas[0] if colunas_numericas else df.columns[0]
col_cat = df.select_dtypes(include=['object']).columns[0] if len(df.select_dtypes(include=['object']).columns) > 0 else col_y

# Criação de gráficos interativos com Plotly
fig_hist = px.histogram(df, x=col_y, title=f'Distribuição de {col_y}', color_discrete_sequence=['teal'])
fig_bar = px.bar(df[col_cat].value_counts().head(10), title=f'Top 10 - {col_cat}', color_discrete_sequence=['purple'])

# Inicializa o app Dash
app = dash.Dash(__name__)

app.layout = html.Div(style={'fontFamily': 'Arial', 'padding': '20px'}, children=[
    html.H1("Dashboard de Análise de E-commerce", style={'textAlign': 'center', 'color': '#333'}),
    html.P("Aplicação interativa desenvolvida para visualização de dados estatísticos.", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([dcc.Graph(figure=fig_hist)], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(figure=fig_bar)], style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
    ])
])

if __name__ == '__main__':
    app.run(debug=True)