def get_max_salary(employees):
    if not employees:
        return 0
    max_val = employees[0]['salary']
    for employee in employees:
        if employee['salary'] > max_val:
            max_val = employee['salary']
    return max_val

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 65000},
        {'name': 'Charlie', 'salary': 45000},
        {'name': 'Diana', 'salary': 72000}
    ]
    result = get_max_salary(sample_data)
    print(result)