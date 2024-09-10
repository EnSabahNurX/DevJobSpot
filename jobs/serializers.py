from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "company",
            "description",
            "requirements",
            "salary",
            "location",
            "created_at",
        ]
