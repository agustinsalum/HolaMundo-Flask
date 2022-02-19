
from flask import Flask

def crear_app():
    # Configuración inicial de la app
    app = Flask(__name__)

    # app.add_url_rule('/', 'holaMundo', holaMundo.hola)
    
    @app.route('/')
    def holamundo():
        return 'Hola Mundo!'
    
    return app
