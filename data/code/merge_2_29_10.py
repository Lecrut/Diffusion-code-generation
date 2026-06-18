class Student:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Student('{self.name}')"
def store_students(names_list):
    students_dict = {}
    for student_name in names_list:
        if not isinstance(student_name, str) or len(student_name.strip()) == 0:
            raise ValueError("Invalid student name provided.")
        existing_student = students_dict.get(student_name.strip(), None)
        if existing_student is not None and hasattr(existing_student, 'name'):
            return "Student already exists."
        new_student = Student(student_name.strip())
        students_dict[student_name] = new_student
    return list(students_dict.values())
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    try:
        stored_students = store_students(sample_names)
        for student in stored_students:
            print(student.name)
    except ValueError as e:
        print(f"Error: {e}")