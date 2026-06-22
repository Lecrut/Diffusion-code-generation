def get_max_salary(employees):
    return max(map(lambda emp: emp['salary'] if isinstance(emp.get('salary'), (int, float)) else 0, employees))

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 'unknown'},
        {'name': 'Charlie', 'salary': 120000},
        {'name': 'Diana', 'salary': None},
        {'name': 'Eve', 'salary': 85000}
    ]
    print(get_max_salary(employees))