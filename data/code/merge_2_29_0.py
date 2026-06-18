class StudentNameValidator:
    def validate_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Invalid student name: must be a non-empty string.")
        return True
def add_student(students_list, new_name):
    validator = StudentNameValidator()
    try:
        validator.validate_name(new_name)
        students_list.append(new_name)
        return f"Student '{new_name}' added successfully."
    except ValueError as e:
        raise Exception(f"Failed to add student: {e}")
if __name__ == '__main__':
    current_students = []
    sample_names = ["Alice", "", 123, "   ", "Bob"]
    for name in sample_names:
        try:
            result = add_student(current_students, name)
            print(result)
        except Exception as ex:
            print(f"Error processing '{name}': {ex}")