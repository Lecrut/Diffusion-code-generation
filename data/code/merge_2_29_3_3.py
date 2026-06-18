import time
def create_student_index(students):
    index = {}
    for student in students:
        if not isinstance(student, dict) or 'last_name' not in student:
            continue
        lname = student['last_name'].lower()
        first_names = student.get('first_name', [])
        if isinstance(first_names, str):
            first_names = [first_names]
        for fname in first_names:
            key = (lname.lower(), fname.lower())
            index[key] = lname
    return index
def lookup_student(index, last_name, first_name=None):
    if not isinstance(last_name, str) or len(last_name.strip()) == 0:
        raise ValueError("Invalid last name")
    lname_lower = last_name.lower()
    key = (lname_lower, '')
    result = index.get(key)
    if result and result[1].lower().strip() == lname_lower:
        return [result]
    found_students = []
    for key, stored_lname in index.items():
        if stored_lname.lower().startswith(lname_lower) or lname_lower.startswith(stored_lname.lower()):
            fname_part = ''
            if first_name:
                fmlower = first_name.lower()
                for stored_fname in index[key]:
                    if stored_fname == fmlower or (not fmlower and len(stored_fname) > 0):
                        found_students.append((stored_lname, stored_fname))
            else:
                if lname_lower == key[0]:
                    found_students.append((stored_lname, stored_fname))
    return found_students
def main():
    students = [
        {'first_name': 'Alice', 'last_name': 'Smith'},
        {'first_name': 'Bob', 'last_name': 'Jones'},
        {'first_name': 'Charlie', 'last_name': 'Brown'},
        {'first_name': 'David', 'last_name': 'Williams'},
        {'first_name': 'Eve', 'last_name': 'Smith'},                                       
    ]
    start_time = time.time()
    student_index = create_student_index(students)
    elapsed_time = time.time() - start_time
    print(f"Index generated in {elapsed_time:.6f} seconds")
    print("Sample Index Keys:", list(student_index.keys())[:3])
if __name__ == '__main__':
    main()