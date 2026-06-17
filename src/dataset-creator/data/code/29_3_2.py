import time
def create_student_lookup():
    students = [
        {"first": "Alice", "last": "Smith"},
        {"first": "Bob", "last": "Jones"},
        {"first": "Charlie", "last": "Brown"},
        {"first": "Diana", "last": "Lee"},
        {"first": "Ethan", "last": "Taylor"}
    ]
    lookup = {}
    for student in students:
        last_name = student["last"]
        if last_name not in lookup:
            lookup[last_name] = []
        lookup[last_name].append(student)
    return lookup
def main():
    data_store = create_student_lookup()
    test_queries = ["Smith", "Jones", "Brown", "Taylor", "Unknown"]
    start_time = time.time()
    for last in test_queries:
        if last in data_store:
            print(f"Found {len(data_store[last])} student(s) with last name '{last}'")
        else:
            print(f"No records found for last name '{last}'")
    end_time = time.time()
    total_duration = end_time - start_time
    print(f"\nTotal lookup operations completed in {total_duration:.6f} seconds")
if __name__ == '__main__':
    main()