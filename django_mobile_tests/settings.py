import os
import warnings


warnings.simplefilter('always')

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite'),
    }
}

SITE_ID = 1

# Set in order to catch timezone aware vs unaware comparisons
USE_TZ = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0'

ROOT_URLCONF = 'django_mobile_tests.urls'

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'NAME': 'django',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                    "django.template.context_processors.debug",
                    'django.template.context_processors.request',
                    "django.contrib.auth.context_processors.auth",
                    'django.contrib.messages.context_processors.messages',
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django_mobile.context_processors.flavour",
                    "django_mobile.context_processors.is_mobile",
            ],
            'loaders': [
                ('django_mobile.loader.CachedLoader', (
                    'django_mobile.loader.Loader',
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
        },
    },
]
TEMPLATE_LOADERS = TEMPLATES[0]['OPTIONS']['loaders']
MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_mobile',
    'django_mobile_tests',
)

import django
if django.VERSION < (1, 6):
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
else:
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'
