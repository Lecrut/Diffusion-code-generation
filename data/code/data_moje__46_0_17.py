def find_max_salary(employees):
    return max(employee['salary'] for employee in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 85000},
        {'name': 'Charlie', 'salary': 105000},
        {'name': 'Diana', 'salary': 92000}
    ]
    print(find_max_salary(employees))