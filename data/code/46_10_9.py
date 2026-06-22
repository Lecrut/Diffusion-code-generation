def get_max_salary(employees):
    if not employees:
        return 0
    max_salary = employees[0].get('salary', 0)
    for employee in employees:
        current_salary = employee.get('salary', 0)
        if current_salary > max_salary:
            max_salary = current_salary
    return max_salary

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 60000},
        {'name': 'Charlie', 'salary': 45000},
        {'name': 'Diana', 'salary': 72000}
    ]
    result = get_max_salary(sample_data)
    print(result)