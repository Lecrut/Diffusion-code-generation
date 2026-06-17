class Student:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Student('{self.name}')"
def store_students(names):
    students = []
    for name in names:
        if isinstance(name, str) and len(name.strip()) > 0:
            students.append(Student(name))
    return students
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    student_list = store_students(sample_names)
    for s in student_list:
        print(s.name)