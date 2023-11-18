from django.shortcuts import redirect, render
from .models import ToDo

# Create your views here.

def index(request):
    # retruns all the todo objects from the database
    todo=ToDo.objects.all()
    
    #checking if the request method is post
    if request.method == 'POST':
        new_todo=ToDo(                    #get the 'title' from the post method
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(request , 'index.html', {'todos':todo})   # Render the 'index.html' template with the retrieved ToDo objects


def delete(request, pk):
    todo = ToDo.objects.get(id=pk)   # Get the ToDo object with the specified primary key (id=pk)
    todo.delete()                    # Delete the ToDo object from the database
    return redirect('/')             # Redirect the user to the index page after deleting the ToDo
