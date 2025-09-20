import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Characters, Planets, Species, Favorites

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Modelos disponibles en el panel
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Species, db.session))
    admin.add_view(ModelView(Favorites, db.session))
