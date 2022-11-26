from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__" #Either I can put a list in hear for maually adding some fields ['budy', 'date']