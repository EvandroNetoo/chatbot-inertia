from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from inertia import render


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request: HttpRequest):
        return render(request, 'Index')
