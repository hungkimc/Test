# write a function to generate GUID for new students and add them to the list

import uuid

students = []

def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

# randomly generate a GUID for new students
def generate_guid():
    return uuid.uuid4()

# add new student to the list
def add_new_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)
