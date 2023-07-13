from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password', 'first_name', 'last_name',
                  'date_joined', 'is_superuser', 'email']
        read_only_fields = ('date_joined', )
