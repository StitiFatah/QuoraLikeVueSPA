from .base import *

DEBUG = True
ALLOWED_HOSTS = []
INTERNAL_IPS = [
    'localhost',
]

INSTALLED_APPS += [

    'debug_toolbar'
]


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]


# DEBUG TOOLBAR SETTINGS


def show_toolbar(request):
    True


DEBUG_TOOLBAR_CONFIGS = {

    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}


DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]
