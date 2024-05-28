from flask import Flask, render_template
import pandas as pd
from io import StringIO

app = Flask(__name__)

# Función para cargar el conjunto de datos
def load_dataset():
    df = pd.read_csv('android-adware/TotalFeatures-ISCXFlowMeter.csv') #El cvs no esta en este proyecto por su peso excesivo
    return df

# Carga del conjunto de datos
df = load_dataset()

@app.route('/')
def index():
    # Imprimir los primeros 10 registros en una tabla HTML
    head_table_html = df.head(10).to_html()

    # Obtener la información del DataFrame
    buffer = StringIO()
    df.info(buf=buffer, verbose=True, show_counts=True)  # Eliminar 'null_counts=True'
    info_text = buffer.getvalue()

    return render_template('index.html', head_table_html=head_table_html, info_text=info_text)

if __name__ == '_main_':
    app.run(debug=True)