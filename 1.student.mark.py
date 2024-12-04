
students = []
courses = {}
marks = {}

#number of students
def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append((student_id, student_name, student_dob))  # Store student as tuple

#number of courses
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = course_name  # Store course as key-value pair

#student marks for a specific course
def input_marks():
    course_id = input("Enter course ID to input marks: ")
    if course_id not in courses:
        print("Invalid course ID.")
        return
    
    for student in students:
        student_id, student_name, _ = student
        mark = float(input(f"Enter mark for {student_name} (ID: {student_id}) in {courses[course_id]}: "))
        if course_id not in marks:
            marks[course_id] = {}
        marks[course_id][student_id] = mark  # Store marks as nested dictionary {course_id: {student_id: mark}}

#list all courses
def list_courses():
    print("\nList of Courses:")
    for course_id, course_name in courses.items():
        print(f"ID: {course_id}, Course: {course_name}")

#list all students
def list_students():
    print("\nList of Students:")
    for student in students:
        student_id, student_name, student_dob = student
        print(f"ID: {student_id}, Name: {student_name}, Date of Birth: {student_dob}")

#show marks for a given student and course
def show_student_marks():
    student_id = input("Enter student ID to view marks: ")
    for course_id, course_name in courses.items():
        if course_id in marks and student_id in marks[course_id]:
            student_mark = marks[course_id][student_id]
            print(f"Course: {course_name}, Mark: {student_mark}")
        else:
            print(f"Course: {course_name}, Mark: Not entered")

#interacting with the system
def student_management_system():
    while True:
        print("\nStudent Mark Management System")
        print("1. Input student data")
        print("2. Input course data")
        print("3. Input marks for students")
        print("4. List all courses")
        print("5. List all students")
        print("6. Show student marks for a given course")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_student_marks()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please choose again.")

# Run student management system
if __name__ == "__main__":
    student_management_system()
