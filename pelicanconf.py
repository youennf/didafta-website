#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'youni'
SITENAME = u'Didaf\'Ta!'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

PATH = "."
OUTPUT_PATH = "output"
OUTPUT_RETENTION = ['.git']
STATIC_PATHS = ['static']
PAGE_PATHS = ['content']
ARTICLE_PATHS = ['content']

PLUGINS = []
THEME = 'template-didafta'
BOOTSTRAP_THEME = 'darkly'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
CUSTOM_CSS = 'static/index.css'
FAVICON = 'static/images/skin/favicon.png'
HIDE_SIDEBAR = True
BANNER = False
BANNER_ALL_PAGES = False
SIDELEFT = False
SIDELEFT_ALL_PAGES = False
DISQUS_SITENAME = "didafta.org"
MAIN_ITEMS = (
	('introduction', '', True),
	('presentation', '', True),
	('news', '<p style="text-align:left">Tout est sur notre bouc: <a href="http://www.facebook.com/didafta">http://www.facebook.com/didafta</a></p><br/>', False),
	('musique', '', True),
	('photos', '', True),
	('textes', '', True),
	('design', '', True),
	('contact', '', True))
MENU_ITEMS = (
	('/#/1', 'Presentation'),
	('/#/2', 'News'),
	('/#/3', 'Musique'),
	('/#/4', 'Photos'),
	('/#/5', 'Textes'),
	('/#/6', 'Design'),
	('/#/7', 'Contact'),
	)
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)
LEFT_LINKS = (
			('#', 'navigate-up fa fa-arrow-circle-up fa-lg', 'return false;'),
			('/rss', 'fa fa-rss fa-lg', ''),
			('#', 'fa fa-arrows-alt fa-lg', 'screenfull.toggle(); return false;'),
			('/index.html', 'fa fa-home fa-lg', ''),
			('#', 'navigate-down fa fa-arrow-circle-down fa-lg', 'return false;'),
			)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
