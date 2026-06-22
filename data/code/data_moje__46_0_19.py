def find_max_salary(employees):
    return max(employee['salary'] for employee in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 70000},
        {'name': 'Bob', 'salary': 80000},
        {'name': 'Charlie', 'salary': 75000},
        {'name': 'Diana', 'salary': 90000},
        {'name': 'Eve', 'salary': 65000}
    ]
    max_salary = find_max_salary(employees)
    print(max_salary)