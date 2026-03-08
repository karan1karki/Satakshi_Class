from django.shortcuts import render
from django.views import View

def home_view(request):
    result = None
    name = "ISTN"

    if request.method == "POST":
        first_num = int(request.POST.get("fn"))
        second_num = int(request.POST.get("sn"))
        third_num = int(request.POST.get('tn'))
        operation = request.POST.get("operation")

        calc = calculator_view()

        if operation == "add":
            result = calc.sum(first_num, second_num, third_num)
        elif operation == "subtract":
            result = calc.subtract(first_num, second_num, third_num)
        elif operation == "multiply":
            result = calc.multiply(first_num, second_num, third_num)
        elif operation == "divide":
            result = calc.divide(first_num, second_num, third_num)
        else :
            result  = " unknown operation"
    return render(request, "main.html", {
        "result" : result,
        "name" : name
    })    
    


class calculator_view(View):
    @staticmethod
    def sum(a, b, c):
        return a + b + c
    @staticmethod
    def multiply(a, b, c):
        return a * b * c
    @staticmethod
    def subtract(a, b , c):
        return a - b - c
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
