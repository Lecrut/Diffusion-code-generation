def get_max_salary(employees):
    max_salary = None
    for emp in employees:
        salary = emp.get('salary')
        if salary is not None:
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 112000},
        {'name': 'Charlie', 'salary': 88000},
        {'name': 'Diana', 'salary': 125000},
        {'name': 'Eve', 'salary': 98000}
    ]
    result = get_max_salary(employees)
    print(result)