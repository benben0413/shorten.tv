#!/usr/bin/env python
"""
"""
import sys
sys.path.insert(0, '/home/lucas/www/shorten.tv/shorten-env')

from werkzeug.contrib.fixers import ProxyFix  # needed for http server proxies
from werkzeug.debug import DebuggedApplication

from backend import app  # as application

app.wsgi_app = ProxyFix(app.wsgi_app)  # needed for http server proxies
application = DebuggedApplication(app, True)
