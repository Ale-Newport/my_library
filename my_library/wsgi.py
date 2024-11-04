"""
WSGI config for my_library project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'my_library' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_library.settings')

application = get_wsgi_application()
