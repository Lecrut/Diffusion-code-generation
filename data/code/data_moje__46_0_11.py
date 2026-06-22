def get_max_salary(employees):
    if not employees:
        return 0
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 75000},
        {'name': 'Charlie', 'salary': 62000},
        {'name': 'Diana', 'salary': 81000}
    ]
    result = get_max_salary(employees)
    print(result)