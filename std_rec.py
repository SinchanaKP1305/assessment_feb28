students = []

def add_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("Roll number already exists.\n")
            return

    name = input("Enter Name: ")

    marks = []
    for i in range(1, 6):
        m = float(input("Enter marks for subject " + str(i) + ": "))
        marks.append(m)

    total = sum(marks)
    average = total / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully.\n")


def view_students():
    if len(students) == 0:
        print("No records found.\n")
        return

    print("\n{:<10} {:<15} {:<10} {:<10} {:<10}".format(
        "Roll", "Name", "Total", "Average", "Grade"))
    print("-" * 60)

    for s in students:
        print("{:<10} {:<15} {:<10} {:<10} {:<10}".format(
            s["roll"],
            s["name"],
            s["total"],
            round(s["average"], 2),
            s["grade"]
        ))
    print()


def search_student():
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Details")
            print("-" * 40)
            print("Roll Number :", s["roll"])
            print("Name        :", s["name"])
            print("Marks       :", s["marks"])
            print("Total       :", s["total"])
            print("Average     :", round(s["average"], 2))
            print("Grade       :", s["grade"])
            print("-" * 40)
            return

    print("Student not found.\n")


def class_statistics():
    if len(students) == 0:
        print("No data available.\n")
        return

    total_avg = 0
    highest = students[0]
    lowest = students[0]

    for s in students:
        total_avg += s["average"]

        if s["total"] > highest["total"]:
            highest = s

        if s["total"] < lowest["total"]:
            lowest = s

    class_avg = total_avg / len(students)

    print("\nClass Statistics")
    print("-" * 40)
    print("Total Students :", len(students))
    print("Class Average  :", round(class_avg, 2))
    print("Highest Scorer :", highest["name"], "-", highest["total"])
    print("Lowest Scorer  :", lowest["name"], "-", lowest["total"])
    print("-" * 40)
    print()


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Class Statistics")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        class_statistics()
    elif choice == "5":
        print("Program Ended")
        break
    else:
        print("Invalid choice\n")