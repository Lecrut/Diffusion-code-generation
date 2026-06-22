def get_max_salary(employees):
    if not employees:
        return None
    max_salary = employees[0].get('salary')
    if max_salary is None:
        max_salary = 0
    for employee in employees:
        salary = employee.get('salary')
        if salary is not None and salary > max_salary:
            max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 75000},
        {'name': 'Charlie', 'salary': 62000},
        {'name': 'David', 'salary': 85000}
    ]
    result = get_max_salary(sample_data)
    print(result)