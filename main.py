import csv
import os

FILE_NAME = "students.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Course"])

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, age, course])

    print("Student Added Successfully!")

def view_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        print("\nStudent Records:")
        for row in reader:
            print(row)

def search_student():
    sid = input("Enter Student ID to Search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        found = False
        for row in reader:
            if row and row[0] == sid:
                print("Student Found:", row)
                found = True
                break

        if not found:
            print("Student Not Found!")

def delete_student():
    sid = input("Enter Student ID to Delete: ")

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row and row[0] != sid:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Student Deleted Successfully!")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")