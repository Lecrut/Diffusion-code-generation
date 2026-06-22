def find_max_salary(employees):
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 82000},
        {'name': 'Charlie', 'salary': 68000},
        {'name': 'Diana', 'salary': 91000}
    ]
    result = find_max_salary(employees)
    print(result)