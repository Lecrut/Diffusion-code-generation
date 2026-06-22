def get_max_salary(employees):
    return max((emp['salary'] for emp in employees), default=0)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 120000},
        {'name': 'Charlie', 'salary': 85000},
        {'name': 'Diana', 'salary': 110000}
    ]
    print(get_max_salary(employees))