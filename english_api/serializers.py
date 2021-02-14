from rest_framework import serializers

from .models import Word

class WordSerializer(serializers.ModelSerializer):
    """"serializes the word object"""

    class Meta:
        model = Word
        fields = "__all__"