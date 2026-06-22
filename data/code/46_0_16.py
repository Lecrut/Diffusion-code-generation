def get_max_salary(employees):
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 60000},
        {'name': 'Charlie', 'salary': 75000}
    ]
    result = get_max_salary(employees)
    print(result)