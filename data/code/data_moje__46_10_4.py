def get_max_salary(employees):
    if not employees:
        return 0
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 70000},
        {'name': 'Bob', 'salary': 85000},
        {'name': 'Charlie', 'salary': 60000}
    ]
    result = get_max_salary(employees)
    print(result)