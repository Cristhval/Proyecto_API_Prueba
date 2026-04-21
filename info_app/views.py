import requests
from django.http import JsonResponse


def saludo(request):
    """
    Endpoint: /api/saludo/

    Método: GET

    Descripción:
    Devuelve un mensaje de saludo en formato JSON.

    Parámetros opcionales:
    - nombre (string): Nombre del usuario

    Ejemplo:
    /api/saludo/?nombre=Cris

    Respuesta:
    {
        "mensaje": "Hola Cris, bienvenido a mi API",
        "autor": "Cristhian"
    }
    """

    nombre = request.GET.get("nombre", "usuario")

    data = {
        "mensaje": f"Hola {nombre}, bienvenido a mi API",
        "autor": "Cristhian"
    }

    return JsonResponse(data)


def chiste(request):
    url = "https://v2.jokeapi.dev/joke/Any?lang=es"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Hay dos tipos de chistes
        if data["type"] == "single":
            return JsonResponse({
                "chiste": data["joke"]
            })
        else:
            return JsonResponse({
                "setup": data["setup"],
                "punchline": data["delivery"]
            })
    else:
        return JsonResponse({"error": "No se pudo obtener el chiste"})