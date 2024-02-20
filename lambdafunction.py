import json

def lambda_handler(event, context):
    # Créer la réponse HTTP
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*",  # Autorise toutes les origines (CORS)
        },
        "body": "<h1>Bienvenue sur mon site statique S3 !</h1>"
    }
    
    return response
