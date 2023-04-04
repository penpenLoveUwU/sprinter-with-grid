from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "kjdanskdjbamsdbakjsndklan"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    from . import sprintr
    app.register_blueprint(sprintr.bp)
    CORS(app)
    return app

