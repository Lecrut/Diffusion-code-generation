import sys
class StudentManager:
    def __init__(self):
        self._students = {}
    def add_student(self, name: str) -> bool:
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        clean_name = name.strip()
        for existing in self._students.values():
            if existing['name'].lower() == clean_name.lower():
                print(f"Error: Student '{clean_name}' already exists.")
                return False
        student_data = {
            'id': len(self._students) + 1,
            'name': clean_name,
            'status': 'active'
        }
        self._students[clean_name] = student_data
        print(f"Success: Added '{clean_name}' with ID {student_data['id']}.")
        return True
    def get_student(self, name: str) -> dict | None:
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        clean_name = name.strip()
        if clean_name in self._students:
            return self._students[clean_name]
        else:
            print(f"Error: Student '{clean_name}' not found.")
            return None
    def validate_student(self, name: str) -> bool:
        try:
            student = self.get_student(name)
            if student is None or 'name' not in student:
                return False
            original_input = name.strip()
            if len(original_input) != len(student['name']):
                print(f"Warning: Input length mismatch for '{original_input}'.")
            return True
        except Exception as e:
            print(f"Validation error: {e}")
            return False
def main():
    manager = StudentManager()
    sample_names = [
        "Alice Johnson",
        "Bob Smith",
        "",
        "  Charlie Brown  ",
        "alice johnson",                                   
        None,
        ""
    ]
    for name in sample_names:
        if manager.add_student(name):
            pass
        print("---")
        result = manager.get_student("Alice Johnson")
        if result is not None:
            print(f"Retrieved {result['name']} (ID: {result['id']})")
            validation_result = manager.validate_student(result['name'])
            print(f"Validation for '{result['name']}': {'Valid' if validation_result else 'Invalid'}")
if __name__ == '__main__':
    main()