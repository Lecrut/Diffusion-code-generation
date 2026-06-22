def get_max_salary(employees):
    max_salary = None
    for employee in employees:
        salary = employee.get('salary')
        if salary is not None:
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_employees = [
        {'name': 'Alice', 'salary': 85000},
        {'name': 'Bob', 'salary': 92000},
        {'name': 'Charlie', 'salary': 78000},
        {'name': 'Diana', 'salary': 105000}
    ]
    result = get_max_salary(sample_employees)
    print(result)