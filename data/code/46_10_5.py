def get_max_salary(employees):
    if not employees:
        return None
    max_salary = employees[0].get('salary', 0)
    for employee in employees:
        salary = employee.get('salary', 0)
        if salary > max_salary:
            max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 75000},
        {'name': 'Charlie', 'salary': 60000}
    ]
    result = get_max_salary(sample_data)
    print(result)