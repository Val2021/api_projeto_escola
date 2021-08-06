from django.db import models
from django.db.models import fields
from escola.models import Aluno, Curso
from djangorestframework import serializers

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome','cpf','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Curso
        fields = '__all__'
