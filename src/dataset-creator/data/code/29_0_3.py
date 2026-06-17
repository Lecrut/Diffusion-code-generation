def validate_and_add(name):
    if not isinstance(name, str) or name.strip() == "":
        return False
    students = []
    try:
        index = students.index(name)
        print(f"Student '{name}' already exists at index {index}.")
        return True
    except ValueError:
        pass
    students.append(name)
    print(f"'{name}' added successfully.")
    return True
if __name__ == '__main__':
    sample_names = ["Alice", "", 123, "Bob", None]
    for name in sample_names:
        result = validate_and_add(name)