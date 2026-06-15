def find_students_by_prefix(student_records, prefix):
    return [student for student in student_records if student.get('name', '').startswith(prefix)]
if __name__ == '__main__':
    student_data = [
        {'id': 101, 'name': 'Alice Smith', 'grade': 'A'},
        {'id': 102, 'name': 'Bob Johnson', 'grade': 'B'},
        {'id': 103, 'name': 'Charlie Brown', 'grade': 'C'},
        {'id': 104, 'name': 'Alice Williams', 'grade': 'A'},
        {'id': 105, 'name': 'David Lee', 'grade': 'B'}
    ]
    search_prefix = 'A'
    results = find_students_by_prefix(student_data, search_prefix)
    print(results)
    search_prefix_2 = 'B'
    results_2 = find_students_by_prefix(student_data, search_prefix_2)
    print(results_2)
    search_prefix_3 = 'Z'
    results_3 = find_students_by_prefix(student_data, search_prefix_3)
    print(results_3)