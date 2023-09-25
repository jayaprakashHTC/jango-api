from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    return Response({'message':'Hello world'})

# Create your views here.
