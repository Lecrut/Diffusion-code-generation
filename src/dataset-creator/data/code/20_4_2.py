import time
student_names = {
    "Alice Smith",
    "Bob Johnson",
    "Charlie Brown",
    "Alice Smith",
    "Diana Prince",
    "Bob Johnson",
    "Eve Adams"
}
def find_names(target):
    found = []
    for name in student_names:
        if target in name:
            found.append(name)
    return found
if __name__ == '__main__':
    print("Original set of unique student names (stored as a set for uniqueness):")
    print(student_names)
    print("-" * 30)
    print("Checking for 'Alice Smith':")
    result1 = [name for name in student_names if name == "Alice Smith"]
    print(result1)
    print("-" * 30)
    print("Checking for 'Bob Johnson':")
    result2 = [name for name in student_names if name == "Bob Johnson"]
    print(result2)
    print("-" * 30)
    print("Checking for a non-existent name 'Frank':")
    result3 = [name for name in student_names if "Frank" in name]
    print(result3)
    print("-" * 30)