# coding=utf-8
import django

__version__ = '0.2.0-dev1'

if django.VERSION < (3, 2):
    default_app_config = 'easy_pdf.apps.EasyPDFConfig'
