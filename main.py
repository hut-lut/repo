"""
Web Front end to Cgminer-python
Written by: Setkeh setkeh <at> gmail <dot> com
https://github.com/setkeh
"""

# Import CherryPy global namespace
import cherrypy
from scripts.cgminerversion import * 

class Root():
    
    @cherrypy.expose
    def index(self):
	    return '''<html>
	    <head>
	    <title>Cgminer Python Stats</title>
	    </head>
	    <body>'''

    @cherrypy.expose
    def header(self):
	    return '''<center><h1>Cgminer - Python Stats</h1></center>'''

    @cherrypy.expose
    def cgversion(self):
	    return '''<Center><p>Cgminer Version: </p></center>''', cg_version()

    @cherrypy.expose
    def footer(self):
	    return '''</body></html>'''

import os.path
mainconf = os.path.join(os.path.dirname(__file__), 'main.conf')

if __name__ == '__main__':
    cherrypy.quickstart(Root(), config=mainconf)
else:
    cherrypy.tree.mount(Root(), config=mainconf)
