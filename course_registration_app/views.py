from django.shortcuts import render
from django.http import JsonResponse
from .models import CourseRegistration
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def register(request):
  try:
    if request.method=="POST":
      data=json.loads(request.body)
      student=CourseRegistration.objects.create(
      name=data["name"],
      email=data["mail"],
      course=data["course"],
      phone=data["phone"]
      )
      return JsonResponse({"status":"success","message":"registration successful"},status=201)
    return JsonResponse({"status":"failed","message":"client side error"},status=400)
  except Exception as e:
    return JsonResponse({"status":"failed","message":e})

def registrations(request):
  try:
    if request.method=="GET":
      data=list(CourseRegistration.objects.values())
      return JsonResponse({"registrartions":data},status=200)
    return JsonResponse({"status":"failed","message":"client side error"},status=500)

  except Exception as e:
    JsonResponse({"status":"failed","message":e},status=500)
