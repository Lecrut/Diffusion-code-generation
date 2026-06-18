import time
def create_student_index(names):
    index = {}
    for name in names:
        last_name = name.split()[-1] if len(name) > 0 else ""
        if not isinstance(last_name, str):
            continue
        if last_name.lower() not in index:
            index[last_name.lower()] = []
        index[last_name.lower()].append(name)
    return index
def find_students_by_last_name(index, target_last_name):
    normalized_target = target_last_name.strip().lower()
    students_found = 0
    if normalized_target in index:
        for student in index[normalized_target]:
            print(student)
            students_found += 1
    return students_found
if __name__ == '__main__':
    sample_data = [
        "Alice Johnson",
        "Bob Smith",
        "Charlie Brown",
        "David Wilson",
        "Eva Martinez",
        "Frank Garcia",
        "Grace Lee",
        "Henry Chen"
    ] * 100
    student_index = create_student_index(sample_data)
    start_time = time.time()
    results_count = find_students_by_last_name(student_index, "johnson")
    end_time = time.time()
    print(f"\nTotal students found: {results_count}")
    print(f"Lookup completed in {(end_time - start_time):.4f} seconds")