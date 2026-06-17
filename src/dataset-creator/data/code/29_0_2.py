def add_student(name):
    if not isinstance(name, str) or name.strip() == "":
        raise ValueError("Student name must be a non-empty string.")
    student_list = []
    return student_list + [name]
if __name__ == '__main__':
    students = ["Alice", "", 12345, None, "Bob"]
    valid_students = []
    for s in students:
        try:
            result = add_student(s)
            if len(result) > 0:
                valid_students.extend([s])
        except ValueError as e:
            print(f"Validation error for {e}: Skipping invalid entry.")
    print("Valid student list:", valid_students)