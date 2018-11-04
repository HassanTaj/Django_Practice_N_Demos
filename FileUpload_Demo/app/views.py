"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


def fileupload(req):
	return render(
		req,
		'app/fileupload.html',
		{
			'title' :'file upload page'
		}
	)