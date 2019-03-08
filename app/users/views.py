# Create your views here.
from django.shortcuts import render
from rest_framework import generics

from users.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the database"""
    serializer_class = UserSerializer
