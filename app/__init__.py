from flask import Flask

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_pw import Peewee
from flask_login import LoginManager

from config import config


bootstrap = Bootstrap()
moment = Moment()
db = Peewee()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    app.cli.add_command(db.cli, 'db')
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .baike import baike as baike_blueprint
    app.register_blueprint(baike_blueprint)

    from .new import new as new_blueprint
    app.register_blueprint(new_blueprint)

    from .video import video as video_blueprint
    app.register_blueprint(video_blueprint)

    return app
