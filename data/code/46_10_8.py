def get_max_salary(employees):
    return max(employee['salary'] for employee in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 85000},
        {'name': 'Charlie', 'salary': 120000},
        {'name': 'Diana', 'salary': 105000}
    ]
    print(get_max_salary(employees))