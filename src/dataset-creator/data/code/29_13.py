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
        index = int(index.strip()) if isinstance(index, str) else int(index)
        if not (0 <= index < len(students)):
            print(f"Index {index} out of range.")
            return None
        return students[index]
    except ValueError:
        print("Invalid index format.")
        return None
def validate_student(name: str) -> bool:
    if not name or not isinstance(name, str):
        return False
    for char in name:
        if not (char.isalpha() or ' ' == char):
            return False
        if len(char.strip()) > 0 and ord(char) < 65 or ord(char) > 122:
            return False
    return True
students = []
if __name__ == '__main__':
    sample_names = ["Alice", "Bob Smith", "Charlie O'Connor"]
    for name in sample_names:
        if add_student(name):
            print(f"Added: {name}")
        retrieved_name = retrieve_student(len(students) - 1)
        if retrieved_name is not None:
            print(f"Retrieved at index {len(students)-1}: {retrieved_name}")
    validation_tests = ["", "John Doe!", "Mary Jane"]
    for test in validation_tests:
        result = validate_student(test)
        status = "Valid" if result else "Invalid"
        print(f"{test} -> {status}")