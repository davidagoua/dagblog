import dj_database_url

from dagblog.settings import *


SECRET_KEY = os.environ.get('SECRET_KEY', "+rns7g79j9b3!t4m0g^bym0+rd!(f_yc@82e556s(p6*m_bh7(")

DEBUG = False
ALLOWED_HOSTS = [
    'dagblog.herokuapp.com'
]

MIDDLEWARE += ['whitenoise.midlleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))
