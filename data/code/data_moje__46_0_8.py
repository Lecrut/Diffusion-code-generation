def find_max_salary(employees):
    return max(employee['salary'] for employee in employees)

if __name__ == '__main__':
    employees_list = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 62000},
        {'name': 'Charlie', 'salary': 55000},
        {'name': 'Diana', 'salary': 78000}
    ]
    result = find_max_salary(employees_list)
    print(result)