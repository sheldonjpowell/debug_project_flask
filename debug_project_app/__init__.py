from flask import Flask

from config import Config

# Import for Flask Db and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import for Flask Mail
from flask_mail import Mail, Message

# Import for Flask Login
from flask_login import LoginManager

# Create flask app variable
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail = Mail(app)

# Login Config
login = LoginManager(pp)
login.login_view = 'login' # Specify what page to load for NON-authenticated Users



from debug_project_app import routes,models