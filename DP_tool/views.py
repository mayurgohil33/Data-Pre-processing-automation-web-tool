from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .models import FilesUpload
import pandas as pd
import numpy as np
import os
from sklearn.impute import SimpleImputer
# Create your views here.

global a
global b

def home(request):
    return render(request,"Home.html")

def Automate(request):
    if request.method == "GET":
        return render(request, "Automate.html")

def show(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        a = pd.read_csv(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        print(a)
        os.remove(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        #return redirect(request,"Automate.html",{'a':a})
        return render(request,"Automate.html",{'a':a})
    
def test():
    print(a)
    
def transform(request):
    if request.method == "POST":
        file3 = request.FILES["file"]
        document1 = FilesUpload.objects.create(file=file3)
        document1.save()
        c = pd.read_csv(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        c.replace("?",np.nan, inplace = True)
        imputer_mode = SimpleImputer(missing_values= np.nan, strategy="most_frequent")
        c[["Gender","Height","Weight"]] = imputer_mode.fit_transform(c[["Gender","Height","Weight"]])
        #print(c)
        os.remove(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        #return redirect(request,"Automate.html",{'a':a})
        return render(request,"Automate.html",{'c':c})
    
def Manual(request):
    if request.method == "GET":
        return render(request, "Manual.html")
    
def display(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        b = pd.read_csv(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        os.remove(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        return render(request,"Manual.html",{'b':b})

def describe(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        a = pd.read_csv(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        d = a.describe()
        return render(request,"Manual.html",{'d':d})

def datatype(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        a = pd.read_csv(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        f = a.dtypes()
        return render(request,"Manual.html",{'f':f})

def missing(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        a = pd.read_csv(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        h = a.isnull()
        return render(request,"Manual.html",{'h':h})
    '''    null_values = a.isnull()
        for i in a:
            print(i)
            print(null_values[i].value_counts())
            print(" ")
            h = null_values[i].value_counts()
            return render(request,"Manual.html",{'h':h})'''
    
def cleaning(request):
    if request.method == "POST":
        return render(request,"Cleaning.html")
    
def fill(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        b = pd.read_csv(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        Column = request.post["Column"]
        repleacable_value = request.post["repleacable value"]
        desired_Value = request.post["desired Value"]
        imputer_mean = SimpleImputer(missing_values = np.nan, strategy = "mean")
        imputer_median = SimpleImputer(missing_values = np.nan, strategy = "median")
        imputer_mode = SimpleImputer(missing_values = np.nan, strategy = "most_frequent")
        imputer_constant = SimpleImputer(missing_values = np.nan, strategy = "{desired_Value}")
        if desired_Value == "mean":
            b.replace("{repleacable_value}",np.nan, inplace = True)
            b[["{Column}"]] = imputer_mean.fit_transform(a[["{Column}"]])
        elif desired_Value == "median":
            a.replace("{repleacable_value}",np.nan, inplace = True)
            a[["{Column}"]] = imputer_median.fit_transform(a[["{Column}"]])
        elif desired_Value == "most_frequent":
            a.replace("{repleacable_value}",np.nan, inplace = True)
            a[["{Column}"]] = imputer_mode.fit_transform(a[["{Column}"]])
        else:
            a["{Column}"].replace("repleacable_value",np.nan, inplace = True)
            a[["{Column}"]] = imputer_constant.fit_transform(a[["{Column}"]])
        os.remove(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        return render(request,"Cleaning.html",{'b':b})

def type(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file=file2)
        document.save()
        c = pd.read_csv(r"C:\Users\Ramesh\Django_projects\Preprocessing_tool\media\test1.csv")
        Column = request.post["Column"]
        desired_datatype = request.post["desired Value"]
        c["{Column}"].astype("{desired_datatype}")

def head(request):
    if request.method == "GET":
        b = b.head()
        return render(request, "Manual.html",{'b':b})