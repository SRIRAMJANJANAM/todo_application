from django.shortcuts import render, redirect
import time
todo_list = []

def task_list(request):
    return render(request, 'testapp/task_list.html', {'tasks': todo_list})

def add_task(request):
    if request.method == "POST":
        task = request.POST['title']
        todo_list.append(task)
        return redirect('task_list')
    return render(request, 'testapp/add.html')

def edit_task(request, task_id):
    task_id = int(task_id) - 1  
    if request.method == "POST":
        new_task = request.POST['title']
        if 0 <= task_id < len(todo_list):
            todo_list[task_id] = new_task
        return redirect('task_list')
    return render(request, 'testapp/edit.html', {'task': todo_list[task_id], 'task_id': task_id + 1})

def delete_task(request, task_id):
    task_id = int(task_id) - 1  
    if 0 <= task_id < len(todo_list):
        todo_list.pop(task_id)
        time.sleep(2)
    return redirect('task_list')
