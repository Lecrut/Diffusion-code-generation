import sys
def add_student(name: str) -> bool:
    if not name.strip():
        return False
    cleaned_name = name.strip()
    for char in cleaned_name:
        if not (char.isalpha() or ' ' == char):
            print(f"Invalid character '{char}' found.")
            return False
    students.append(cleaned_name)
    return True
def get_student(index: int) -> str | None:
    try:
        student_index = index - 1
        if not (0 <= student_index < len(students)):
            print(f"Index {index} out of range.")
            return None
        return students[student_index]
    except Exception as e:
        print(f"Error retrieving student: {e}")
        return None
def validate_student(name: str) -> bool:
    if not isinstance(name, str):
        print("Name must be a string.")
        return False
    name = name.strip()
    if len(name) < 2 or len(name) > 50:
        print(f"Name length must be between 2 and 50 characters. Got {len(name)}.")
        return False
    for char in name:
        if not (char.isalpha()):
            print("Name contains non-alphabetic characters.")
            return False
    return True
students = []
if __name__ == '__main__':
    sample_names = ["Alice", "Bob Smith", "Charlie123"]
    for name in sample_names:
        if add_student(name):
            print(f"Added {name}")
        result = get_student(0)
        if result is not None:
            print(f"Retrieved student at index 0: {result}")
        validation_result = validate_student("David")
        if validation_result:
            print("Validation passed for David.")