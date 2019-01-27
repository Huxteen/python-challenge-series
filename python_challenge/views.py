from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import string


# Create your views here.
def home(request):
    return render(request, 'home.html')

# A function that sort a string alphabetically and remove punctuations and empty spaces
def sort_and_remove_duplicate(request):
    if request.method == 'POST':
        sort_input = request.POST['sort_and_remove_duplicate'] # collecs form data
        exclude_punctuations = str.maketrans({key: None for key in string.punctuation})
        format_input = "".join(sorted(set(sort_input.casefold().replace(' ', ''))))
        sort_output = format_input.translate(exclude_punctuations)  # exclude punctuations
        return render(request, 'home.html', {'sort_input': sort_input, 'sort_output': sort_output})
    else:
        messages.error(request, 'Hello Boss. Please, submit the form properly')
        return redirect('/')


# A function that finds the factoria of a number
def find_factoria(request):
    if request.method == 'POST':
        factoria_input = int(request.POST['factoria'])
        var_input = factoria_input
        factoria_output = 1
        if factoria_input <= 0:
            messages.error(request, 'Hello Boss. We cant have a factoria of a number less than 1')
            return render(request, 'factoria.html')
        else:
            while var_input > 0:
                factoria_output = factoria_output * var_input
                var_input = var_input - 1
            return render(request, 'factoria.html', {'factoria_output': factoria_output, 'factoria_input': factoria_input})
    else:
        messages.error(request, 'Hello Boss. Please, submit form properly')
        return render(request, 'factoria.html')


