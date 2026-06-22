def get_maximum_salary(employees):
    return max(employee['salary'] for employee in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 85000},
        {'name': 'Charlie', 'salary': 65000}
    ]
    max_salary = get_maximum_salary(employees)
    print(max_salary)