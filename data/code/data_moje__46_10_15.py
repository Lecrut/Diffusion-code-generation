def get_max_salary(employees):
    return max(employee.get('salary', 0) for employee in employees)

if __name__ == '__main__':
    sample_employees = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 82000},
        {'name': 'Charlie', 'salary': 68000},
        {'name': 'Diana', 'salary': 91000},
        {'name': 'Eve', 'salary': 78000}
    ]
    print(get_max_salary(sample_employees))