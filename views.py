# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:30:41 2021

@author: Win10Pro
"""

from jango.http import HttpResponse

def about(request):
    return HttpResponse('This is about page')