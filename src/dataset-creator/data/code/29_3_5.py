import time
def create_student_index():
    students = [
        {"first": "Alice", "last": "Smith"},
        {"first": "Bob", "last": "Jones"},
        {"first": "Charlie", "last": "Brown"},
        {"first": "Diana", "last": "Williams"},
        {"first": "Ethan", "last": "Taylor"}
    ]
    index = {}
    for student in students:
        last_name = student["last"]
        if last_name not in index:
            index[last_name] = []
        index[last_name].append(student)
    return index, len(students), sum(len(v) for v in index.values())
def benchmark_lookup(index):
    start_time = time.time()
    target_last_names = ["Smith", "Jones", "NonExistent"]
    results = []
    for last_name in target_last_names:
        if last_name in index:
            students_list = index[last_name]
            print(f"Found {len(students_list)} student(s) with last name '{last_name}'")
            for s in students_list:
                results.append((s["first"], s["last"]))
        else:
            print(f"No records found for last name '{last_name}'")
    end_time = time.time()
    duration = end_time - start_time
    total_lookups = len(target_last_names)
    return {
        "total_records": sum(len(v) for v in index.values()),
        "unique_last_names": len(index),
        "lookup_duration_ms": round(duration * 1000, 3),
        "results_per_second": round(total_lookups / duration, 2) if duration > 0 else float('inf')
    }
if __name__ == '__main__':
    index, total_records, unique_last_names = create_student_index()
    print(f"Total students: {total_records}")
    print(f"Unique last names in database: {unique_last_names}")
    print("\nRunning lookup benchmark...")
    stats = benchmark_lookup(index)
    print("\nBenchmark Results:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")