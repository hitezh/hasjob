# -*- coding: utf-8 -*-
import os

#: The title of this site
SITE_TITLE = 'Job Board'
#: Database backend
SQLALCHEMY_DATABASE_URI = 'postgres://127.0.0.1/hasjob'
SERVER_NAME = 'hasjob.travis.local:5000'
#: LastUser server
LASTUSER_SERVER = 'https://auth.hasgeek.com/'
#: LastUser client id
LASTUSER_CLIENT_ID = os.environ.get('LASTUSER_CLIENT_ID')
#: LastUser client secret
LASTUSER_CLIENT_SECRET = os.environ.get('LASTUSER_CLIENT_SECRET')
