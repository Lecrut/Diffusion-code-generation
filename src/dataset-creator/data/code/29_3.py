import time
def create_student_lookup():
    students = [
        {"first": "Alice", "last": "Smith"},
        {"first": "Bob", "last": "Jones"},
        {"first": "Charlie", "last": "Brown"},
        {"first": "Diana", "last": "Davis"},
        {"first": "Eve", "last": "Wilson"}
    ]
    lookup = {}
    for student in students:
        last_name = student["last"]
        if last_name not in lookup:
            lookup[last_name] = []
        lookup[last_name].append(student)
    return lookup
def test_lookup_performance():
    data = create_student_lookup()
    iterations = 10000
    start_time = time.perf_counter()
    for _ in range(iterations):
        target_last = "Smith"
        result = data.get(target_last, [])
        assert len(result) > 0 and result[0]["first"] == "Alice", "Lookup failed or incorrect data returned."
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"Performed {iterations} lookups in {elapsed:.4f} seconds.")
if __name__ == '__main__':
    test_lookup_performance()