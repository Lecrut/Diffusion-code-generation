def store_student_names(names):
    student_set = set()
    for name in names:
        student_set.add(name)
    return student_set
if __name__ == '__main__':
    sample_names = [
        "Alice",
        "Bob",
        "Charlie",
        "Alice",
        "David",
        "Bob",
        "Eve"
    ]
    unique_students = store_student_names(sample_names)
    print(f"Original list: {sample_names}")
    print(f"Unique student names (Set): {unique_students}")