def get_max_salary(employees):
    if not employees:
        return None
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    sample_employees = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 75000},
        {'name': 'Charlie', 'salary': 62000}
    ]
    result = get_max_salary(sample_employees)
    print(result)