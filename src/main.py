import os
import pandas as pd
import openai
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno del archivo .env

def cargar_datos(filepath):
    return pd.read_csv(filepath)

def analizar_datos(datos):
    print(datos.describe())  # Un análisis simple

def generar_sugerencias_ia(datos):
    # Supongamos que 'datos' contiene estadísticas sobre el uso de recursos
    descripción_datos = "Resumen de datos: " + datos.describe().to_string()
    prompt = descripción_datos + " ¿Cuáles son las mejores estrategias para mejorar la utilización de recursos en el hospital?"

    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100  # Ajusta según sea necesario
    )
    return response.choices[0].text.strip()



def main():
    datos = cargar_datos("./data/datos_hospital.csv")
    analizar_datos(datos)
    sugerencia = generar_sugerencias_ia(datos)
    print("Sugerencia de IA:", sugerencia)

if __name__ == "__main__":
    main()
