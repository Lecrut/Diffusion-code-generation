def find_max_salary(employees):
    return max(map(lambda emp: float(emp['salary']) if isinstance(emp.get('salary'), (int, float, str)) and str(emp['salary']).replace('.', '', 1).lstrip('-').isdigit() else float('-inf'), employees))

if __name__ == '__main__':
    sample_employees = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': '95000'},
        {'name': 'Charlie', 'salary': 'N/A'},
        {'name': 'Diana', 'salary': 120000.5},
        {'name': 'Eve', 'salary': 'invalid'}
    ]
    result = find_max_salary(sample_employees)
    print(result)