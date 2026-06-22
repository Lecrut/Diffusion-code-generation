def get_max_salary(employees):
    if not employees:
        return None
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    employee_list = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 75000},
        {'name': 'Charlie', 'salary': 62000},
        {'name': 'Diana', 'salary': 88000}
    ]
    max_sal = get_max_salary(employee_list)
    print(max_sal)