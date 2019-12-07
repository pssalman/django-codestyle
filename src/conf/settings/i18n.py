from django.utils.translation import ugettext_lazy as _

try:
    from .base import LOCALE_ROOT, MIDDLEWARE
except ImportError:
    print('Unable to import base settings file:')

LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'Asia/Jerusalem'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# This list of languages will be provided
LANGUAGES = [
    ('ar', gettext_noop('Arabic')),
    ('ca', gettext_noop('Catalan')),
    ('cs', gettext_noop('Czech')),
    ('da', gettext_noop('Danish')),
    ('de', gettext_noop('German')),
    ('en-us', gettext_noop('English')),
    ('el', gettext_noop('Greek')),
    ('es', gettext_noop('Spanish')),
    ('fi', gettext_noop('Finnish')),
    ('fr', gettext_noop('French')),
    ('he', gettext_noop('Hebrew')),
    ('it', gettext_noop('Italian')),
    ('ko', gettext_noop('Korean')),
    ('nl', gettext_noop('Dutch')),
    ('pl', gettext_noop('Polish')),
    ('pt', gettext_noop('Portuguese')),
    ('pt-br', gettext_noop('Brazilian Portuguese')),
    ('ro', gettext_noop('Romanian')),
    ('ru', gettext_noop('Russian')),
    ('sk', gettext_noop('Slovak')),
    ('uk', gettext_noop('Ukrainian')),
    ('zh-cn', gettext_noop('Simplified Chinese')),
]

LANGUAGES_BIDI = ['he', 'ar']

# Tell Django where the project's translation files should be.
LOCALE_PATHS = (
    LOCALE_ROOT,
)

# Inject the localization middleware into the right position
MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('django.middleware.locale.LocaleMiddleware', x) if MIDDLEWARE[i-1] ==     'django.contrib.sessions.middleware.SessionMiddleware' else (x, ))]
