class Student:
    def __init__(self, name):
        self.name = name
def store_students(names_list):
    students_dict = {}
    for idx in range(len(names_list)):
        student_obj = Student(names_list[idx])
        students_dict[f"student_{idx}"] = student_obj
    return students_dict
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    stored_data = store_students(sample_names)
    for key, value in stored_data.items():
        print(f"{key}: {value.name}")