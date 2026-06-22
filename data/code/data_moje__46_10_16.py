def get_max_salary(employees):
    max_sal = float('-inf')
    for emp in employees:
        sal = emp['salary']
        if sal > max_sal:
            max_sal = sal
    return max_sal

if __name__ == '__main__':
    data = [
        {'name': 'Alice', 'salary': 85000},
        {'name': 'Bob', 'salary': 92000},
        {'name': 'Charlie', 'salary': 78000},
        {'name': 'Diana', 'salary': 105000}
    ]
    result = get_max_salary(data)
    print(result)