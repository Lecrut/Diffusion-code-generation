import time
def create_student_index(students):
    index = {}
    for student in students:
        if 'last_name' not in student:
            continue
        lname = student['last_name'].lower()
        first_names = [s.get('first_name', '').strip().title() for s in students 
                       if s.get('last_name').lower() == lname]
        existing_list = index.get(lname, [])
        new_entry = [f"{s['first_name'].strip().title()} {lname}" for s in students if s.get('last_name').lower() == lname]
        seen_names = set(existing_list)
        unique_new_entries = [name for name in new_entry if name not in seen_names]
        index[lname] = existing_list + unique_new_entries
    return index
def lookup_student(index, last_name):
    lname_lower = last_name.lower()
    return index.get(lname_lower) or []
if __name__ == '__main__':
    raw_students = [
        {'first_name': 'Alice', 'last_name': 'Smith'},
        {'first_name': 'Bob', 'last_name': 'Jones'},
        {'first_name': 'Charlie', 'last_name': 'Smith'},
        {'first_name': 'David', 'last_name': 'Brown'},
        {'first_name': 'Eve', 'last_name': 'Jones'},
        {'first_name': 'Frank', 'last_name': 'Davis'},
    ]
    student_index = create_student_index(raw_students)
    start_time = time.time()
    queries = ['Smith', 'Jones', 'Brown', 'Unknown']
    results = []
    for query in queries:
        res = lookup_student(student_index, query)
        if not isinstance(res, list):
            res = [res]                                                                                                
        results.append({
            'query': query,
            'found_count': len(res),
            'students': res[:3] if len(res) > 3 else res                                                 
        })
    end_time = time.time()
    print(f"Lookup completed in {end_time - start_time:.6f} seconds")
    print("Results:")
    for r in results:
        if len(r['students']) > 0:
            print(f"{r['query']}: {[s.split()[0] + ' ' + s.split()[-1] for s in r['students']]}" ) 
        else:
            print(f"{r['query']}: No records found")
    assert len(lookup_student(student_index, 'Smith')) == 2
    assert lookup_student(student_index, 'Jones') is not None