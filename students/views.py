from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import StudentForm
from .models import Student

def home(request):
    return render(request, "students/home.html")

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect("add_student")
    else:
        form = StudentForm()

    return render(request, "students/add_student.html", {"form": form})

def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})

def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/update_student.html", {"form": form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect("student_list")
