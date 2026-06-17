import time
def create_student_index():
    students = [
        {"first": "Alice", "last": "Smith"},
        {"first": "Bob", "last": "Jones"},
        {"first": "Charlie", "last": "Brown"},
        {"first": "Diana", "last": "Wilson"},
        {"first": "Eve", "last": "Taylor"}
    ]
    index = {}
    for student in students:
        last_name = student["last"]
        if last_name not in index:
            index[last_name] = []
        index[last_name].append(student)
    return index
def lookup_by_last_name(index, last_name):
    return index.get(last_name, [])
if __name__ == '__main__':
    student_index = create_student_index()
    test_queries = ["Smith", "Jones", "Brown", "Wilson"]
    start_time = time.time()
    for name in test_queries:
        results = lookup_by_last_name(student_index, name)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")