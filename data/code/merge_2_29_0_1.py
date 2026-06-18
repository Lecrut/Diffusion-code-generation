def add_student(name):
    if not isinstance(name, str) or name.strip() == "":
        return False
    students.append(name)
    return True
students = []
if __name__ == '__main__':
    test_cases = ["Alice", "", 12345, None, "   ", "Bob"]
    for case in test_cases:
        result = add_student(case)
        print(f"Added '{case}' -> {result}")