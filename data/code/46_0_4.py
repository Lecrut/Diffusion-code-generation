def get_max_salary(employees):
    return max(employee['salary'] for employee in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 75000},
        {'name': 'Charlie', 'salary': 62000},
        {'name': 'Diana', 'salary': 88000}
    ]
    max_salary = get_max_salary(employees)
    print(max_salary)