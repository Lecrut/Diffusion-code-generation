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
def retrieve_student(index: int) -> str | None:
    try:
        index = int(index)
        if not (0 <= index < len(students)):
            print(f"Index {index} out of range.")
            return None
        return students[index]
    except ValueError:
        print("Invalid input type for index.")
        return None
def validate_student(name: str) -> bool:
    if not name or not isinstance(name, str):
        return False
    cleaned_name = name.strip()
    if len(cleaned_name) < 2:
        return False
    has_space = ' ' in cleaned_name
    for char in cleaned_name:
        if not (char.isalpha()):
            return False
    return True
students: list[str] = []
if __name__ == '__main__':
    sample_names = ["Alice", "Bob Smith", "Charlie"]
    print("Adding students...")
    for name in sample_names:
        if add_student(name):
            print(f"Added {name}")
        else:
            print(f"Failed to add {name}")
    retrieved_name = retrieve_student(0)
    if retrieved_name is not None:
        print(f"Retrieved student at index 0: {retrieved_name}")
    validation_result = validate_student("David")
    print(f"Validation result for 'David': {'Valid' if validation_result else 'Invalid'}")