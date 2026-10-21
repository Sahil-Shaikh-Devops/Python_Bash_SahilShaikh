students = {
    "Sahil": 85,
    "Sameer": 92,
    "Faisal": 78
}

name = input("Enter student name: ")
grade = int(input("Enter grade: "))

if name in students:
    students[name] = grade
    print("Student grade updated successfully.")
else:
    students[name] = grade
    print("New student added successfully.")

print("\nAll Student Grades:")
for student, marks in students.items():
    print(f"{student}: {marks}")
