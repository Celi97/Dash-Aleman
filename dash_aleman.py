import dash
from dash import dcc, html, Input, Output, State
import pandas as pd

# ---- Carga de datos ----
df = pd.read_excel("aleman.xlsx")  
df_verbos = pd.read_excel("aleman.xlsx",sheet_name='Verbos') 
# ---- Inicializar app ----
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# ---- Layout principal con pestañas ----
app.layout = html.Div(
    [
        dcc.Tabs(
            id="tabs",
            value="tab-traducciones",
            children=[
                dcc.Tab(label="Traducciones", value="tab-traducciones"),
                dcc.Tab(label="Artículos", value="tab-articulos"),
                dcc.Tab(label="Verbos", value="tab-verbos")
            ],
            style={"fontFamily": "Georgia, sans-serif", "fontSize": "24px", "font-style": "italic"}
        ),
        html.Div(id="tabs-content")
    ],
    style={
        "backgroundColor":  "#fff5cc",
        "fontFamily": "Arial, sans-serif",
        "height": "100vh",
        "padding": "20px"
    }
)

# ---- Callback para renderizar el contenido de cada pestaña ----
@app.callback(
    Output("tabs-content", "children"),
    Input("tabs", "value"),
    
)


def render_content(tab):
    if tab == "tab-traducciones":
        return html.Div(
            [
                html.Img(
                    src="https://www.guiadealemania.com/wp-content/uploads/2011/01/bandera-de-alemania.jpg",
                    style={"width": "300px", "marginBottom": "20px","marginTop":"40px"}  # espacio aumentado
                ),
                html.H1("Traduce la palabra", style={"textAlign": "center", "fontWeight": "lighter", "fontFamily": "Georgia, serif", "fontSize": "24px"}),
                html.Div(id="palabra-random", style={"fontSize": 24, "marginBottom": "20px",}),
                dcc.Input(
                    id="respuesta",
                    type="text",
                    placeholder="Escribe la traducción aquí...",
                    debounce=True,
                    style={"padding": "10px", "fontSize": "18px", "textAlign": "center", "width": "300px", "marginBottom": "20px"}  # margen añadido
                ),
                html.Button(
                    "Nueva palabra",
                    id="btn-new",
                    n_clicks=0,
                    style={
                        "marginTop": "20px",
                        "padding": "15px 40px",
                        "fontSize": "22px",
                        "borderRadius": "10px",
                        "backgroundColor": "#b22222",
                        "color": "#fff",
                        "border": "none",
                        "cursor": "pointer"
                    }
                ),
                html.Div(id="resultado-traduccion", style={"marginTop": "20px", "fontSize": 20, "fontWeight": "bold"}),
                html.Div(
                    "By Celina López",
                    style={
                        "position": "fixed",
                        "bottom": "10px",
                        "left": "10px",
                        "backgroundColor": "#87a5ff",
                        "padding": "10px 15px",
                        "borderRadius": "8px",
                        "boxShadow": "0px 0px 10px rgba(0,0,0,0.2)",
                        "fontSize": "14px",
                        "color": "#333",
                        "fontWeight": "lighter",
                        "fontStyle": "italic"
                    }
                )
            ],
            style={"display": "flex", "flexDirection": "column", "alignItems": "center", "textAlign": "center"}
        )
    
    elif tab == "tab-articulos":
        return html.Div(
            [
                html.Img(
                    src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Falemanologia.s3.eu-west-3.amazonaws.com%2FIm%25C3%25A1genes%2BBlog%2BAlemanologia%2FTabla%2Bde%2BArt%25C3%25ADculos.png&f=1&nofb=1&ipt=a2295b5a23714e900b4963586af1b97ee673b1c93a347259e23562cc71752710",
                    style={"width": "400px", "marginBottom": "20px","marginTop":"40px"}  # más espacio
                ),
                html.H1("¿Cuál es el artículo?", style={"textAlign": "center", "fontWeight": "lighter", "fontFamily": "Georgia, serif"}),
                html.Div(id="articulo-random", style={"fontSize": 24, "marginBottom": "20px"}),
                dcc.Input(
                    id="respuesta",
                    type="text",
                    placeholder="Escribe el artículo aquí...",
                    debounce=True,
                    style={"padding": "10px", "fontSize": "18px", "textAlign": "center", "width": "300px", "marginBottom": "20px"}
                ),
                html.Button(
                    "Nuevo artículo",
                    id="btn-new",
                    n_clicks=0,
                    style={
                        "marginTop": "20px",
                        "padding": "15px 40px",
                        "fontSize": "22px",
                        "borderRadius": "10px",
                        "backgroundColor": "#b22222",
                        "color": "#fff",
                        "border": "none",
                        "cursor": "pointer"
                    }
                ),
                html.Div(id="resultado-articulos", style={"marginTop": "20px", "fontSize": 20, "fontWeight": "bold"}),
                html.Div(
                    "By Celina López",
                    style={
                        "position": "fixed",
                        "bottom": "10px",
                        "left": "10px",
                        "backgroundColor": "#87a5ff",
                        "padding": "10px 15px",
                        "borderRadius": "8px",
                        "boxShadow": "0px 0px 10px rgba(0,0,0,0.2)",
                        "fontSize": "14px",
                        "color": "#333",
                        "fontWeight": "lighter",
                        "fontStyle": "italic"
                    }
                )
            ],
    
            style={"display": "flex", "flexDirection": "column", "alignItems": "center", "textAlign": "center"}
        )
    elif tab == "tab-verbos":
        return html.Div(
            [
                html.H1(
                    "Verbos en alemán",
                    style={
                        "textAlign": "center",
                        "fontWeight": "lighter",
                        "fontFamily": "Georgia, serif"
                    }
                ),
                # Contenedor de tarjetas
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            verb["palabra"],  # Frente
                                            className="card-front"
                                        ),
                                        html.Div(
                                            verb["traduccion"],  # Reverso
                                            className="card-back"
                                        ),
                                    ],
                                    className="card-inner"
                                )
                            ],
                            className="card"
                        )
                        for _, verb in df_verbos.iterrows()
                    ],
                    className="card-grid"
                ),
                html.Div(
                    "By Celina López",
                    style={
                        "position": "fixed",
                        "bottom": "10px",
                        "left": "10px",
                        "backgroundColor": "#87a5ff",
                        "padding": "10px 15px",
                        "borderRadius": "8px",
                        "boxShadow": "0px 0px 10px rgba(0,0,0,0.2)",
                        "fontSize": "14px",
                        "color": "#333",
                        "fontWeight": "lighter",
                        "fontStyle": "italic"
                    }
                )
                
            ]
        )

# ---- Callbacks para la pestaña de traducciones y artículos ----
@app.callback(
    Output("palabra-random", "children"),
    Input("btn-new", "n_clicks")
)
def nueva_palabra(n):
    if n == 0:
        return html.Div(
            "Haz clic en 'Nueva palabra' para empezar",
            style={
                "fontFamily": "Georgia, serif",
                "fontWeight": "lighter",
                "fontSize": "14px",
                "textAlign": "center",
                "color": "#000000"
            }
        )
    fila = df.sample(1).iloc[0]
    return html.Div(
            f"{fila['palabra']}",
            style={
                "fontFamily": "Georgia, serif",
                "fontWeight": "lighter",
                "fontSize": "20px",
                "textAlign": "center",
                "color": "#000000",
                "fontStyle": "italic"
            }
    )

@app.callback(
    Output("resultado-traduccion", "children"),
    Input("respuesta", "n_submit"),
    State("respuesta", "value"),
    State("palabra-random", "children")
)
def comprobar_traduccion(n_submit, respuesta, palabra_texto):
    if not n_submit or not respuesta:
        return ""
    
    palabra = palabra_texto['props']['children']
    traduccion_correcta = df.loc[df["palabra"] == palabra, "traduccion"].values[0]
    
    
    # Considerar correcto si la respuesta coincide con cualquiera de las palabras
    if respuesta.lower() == traduccion_correcta.lower():
        return "✅ ¡Correcto!"
    else:
        return f"❌ Incorrecto. La respuesta correcta es: {traduccion_correcta}"
    

@app.callback(
    Output("articulo-random", "children"),
    Input("btn-new", "n_clicks")
)
def nueva_palabra(n):
    if n == 0:
        return html.Div(
            "Haz clic en 'Nuevo artículo' para empezar",
            style={
                "fontFamily": "Georgia, serif",
                "fontWeight": "lighter",
                "fontSize": "14px",
                "textAlign": "center",
                "color": "#000000"
            }
        )
    fila = df.sample(1).iloc[0]
    return html.Div(
            f"{fila['traduccion'].split(' ')[1]}",
            style={
                "fontFamily": "Georgia, serif",
                "fontWeight": "lighter",
                "fontSize": "20px",
                "textAlign": "center",
                "color": "#000000",
                "fontStyle": "italic"
            }
    )


@app.callback(
    Output("resultado-articulos", "children"),
    Input("respuesta", "n_submit"),
    State("respuesta", "value"),
    State("articulo-random", "children")
)
def comprobar_articulo(n_submit, respuesta, palabra_texto):
    if not n_submit or not respuesta:
        return ""
    
    palabra = palabra_texto['props']['children']

    articulo_correcto = df[df["traduccion"].str.contains(palabra, na=False)]['traduccion'].reset_index(drop=True)[0].split(' ')[0]

    # Considerar correcto si la respuesta coincide con cualquiera de las palabras
    if articulo_correcto.lower() == respuesta.lower():
        return "✅ ¡Correcto!"
    else:
        return f"❌ Incorrecto. La respuesta correcta es: {articulo_correcto}"
    

# ---- Ejecutar app ----
if __name__ == "__main__":
    app.run(debug=True)
