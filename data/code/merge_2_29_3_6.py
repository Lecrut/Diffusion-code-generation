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
    matches = index.get(normalized_target, [])
    if not isinstance(matches, list):
        matches = [matches]
    return matches
if __name__ == '__main__':
    sample_data = ["Alice Johnson", "Bob Smith", "Charlie Brown", "David Lee", "Eva Martinez"]
    student_index = create_student_index(sample_data)
    start_time = time.perf_counter()
    results = find_students_by_last_name(student_index, "johnson")
    end_time = time.perf_counter()
    print(f"Found {len(results)} students for last name: Johnson")
    if isinstance(results[0], list):
        print("Students:", ", ".join(results))
    else:
        print("Student:", results)