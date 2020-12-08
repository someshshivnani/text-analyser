from django.http import HttpResponse
from django.shortcuts import render
from textblob import TextBlob

def index(request):
	return render(request,'adboot.html')

def home(request):
	return render(request,'index.html')
	# return HttpResponse("from home function")

def text_analyse(request):

	txt=request.POST.get('text','default')
	removepunc=request.POST.get('removepun','off')
	cap=request.POST.get('upper','off')
	nline=request.POST.get('newline','off')
	nspace=request.POST.get('space','off')	
	ccount=request.POST.get('ccount','off')
	count=0
	PUNCTUATION ='''!()/[]-{*+}?~%'\^|#><@,$&"'''
	ntxt=''
	
	
	if removepunc=='on':
		if (cap=='on'):
			txt=txt.upper()
		purpose='Remove punctuations is'
		for i in txt:
			if i not in PUNCTUATION:
				ntxt=ntxt+i
	
	elif (cap=='on'):
		purpose='Capitalizing words is'
		if(removepunc=='on'):
			for i in txt:
				if i not in PUNCTUATION:
					ntxt=ntxt+i
		
		ntxt=txt.upper()

	elif (nline=='on'):
		purpose='Removing new lines is '
		for i in txt:
			if i !="\n" and i !='\r':
				ntxt=ntxt+i

	elif(nspace=='on'):
		purpose='Removing Extra Space is'
		for index,char in enumerate(txt):
			if not (txt[index]==' ' and txt[index+1]==' '):
				ntxt=ntxt+char

	elif(ccount=='on'):
		purpose='Counting all characters is'
		for i in txt:
			if not(i==' '):
				count+=1
		ntxt=ntxt+str(count)
	
	parms={
		'analyszed':ntxt,'purpose':purpose
	}
	return render(request,"res.html",parms)
	# return HttpResponse(f"i got <h1>{txt}</h1> from home")

