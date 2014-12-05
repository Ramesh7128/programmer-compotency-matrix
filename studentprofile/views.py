# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from oautherise.forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

def index(request):
    context = RequestContext(request)
    context_dict = {}
    colordict = {
            "datastructures": {
                "level0":5,
                "level1":3,
                "level2":7,
                "level3":8,
            },
            "Algorithms": {

                "level0":0.4,
                "level1":11,
                "level2":5,
                "level3":2,
            },
            "Systems Programming": {

                "level0":6,
                "level1":10,
                "level2":1,
                "level3":2,
            },
            "Source Code Version Control": {

                "level0":0,
                "level1":1,
                "level2":9,
                "level3":11,

            },
            "Build Automation": {

                "level0":.7,
                "level1":.6,
                "level2":.4,
                "level3":.0,

            },
            "Automated testing": {

                "level0":.6,
                "level1":.6,
                "level2":.1,
                "level3":.1,

            },
            "Problem Decomposition": {

                "level0":.2,
                "level1":.6,
                "level2":.9,
                "level3":.1,

            },
            "Systems Decomposition": {

                "level0":.6,
                "level1":.5,
                "level2":.6,
                "level3":.0,

            },
            "Communication": {

                "level0":.5,
                "level1":.3,
                "level2":.6,
                "level3":.9,

            },
            "Code Organization within a file": {

                "level0":.1,
                "level1":1,
                "level2":.6,
                "level3":.4,

            },
            "Code organization across files": {

                "level0":1,
                "level1":2,
                "level2":9,
                "level3":11,

            },
            "Source Tree Orgranization": [3,13,2,4],
            "Code Readability": [3,12,6,2],
            "Defensive Coding": [10,3,5,1],
            "Error handling": [5,8,5,2],
            "IDE": [2,8,7,1],
            "API": [13,4,3,0],
            "Frameworks": [1,9,9,1],
            "Requirements": [2,7,5,5],
            "Scripting": [7,1,11,1],
            "Database": [5,7,5,5],
            "Languages with Professional Experience": [12,5,3,0],
            "Platforms with professional experience": [12,3,2,0],
            "years of professional experience": [7,3,0,0],
            "domain knowledge": [4,9,7,1],
            "tool knowledge": [9,8,5,0],
            "languages exposed to": [11,9,2,0],
            "codebase knowledge": [7,8,6,0],
            "knowledge of upcoming technologies": [3,12,4,1],
            "platform internals": [10,7,2,0],
            "books": [8,8,3,0],
            "blogs": [8,5,5,1],
    }
    context_dict['colordict'] = colordict
    return render_to_response('studentracker/base.html', context_dict, context)