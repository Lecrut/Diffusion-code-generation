class Student:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Student('{self.name}')"
def store_students(names_list):
    students_dict = {}
    for index in range(len(names_list)):
        student_name = names_list[index]
        if not isinstance(student_name, str) or len(student_name.strip()) == 0:
            raise ValueError(f"Invalid name at index {index}: '{student_name}'")
        students_dict[student_name.lower()] = Student(student_name)
    return students_dict
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    student_registry = store_students(sample_names)
    print("Student Registry:")
    for name, student in sorted(student_registry.items()):
        print(f"  {student}")