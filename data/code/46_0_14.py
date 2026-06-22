def find_max_salary(employees):
    if not employees:
        return None
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    employee_list = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 82000},
        {'name': 'Charlie', 'salary': 68000},
        {'name': 'Diana', 'salary': 91000}
    ]
    max_salary = find_max_salary(employee_list)
    print(max_salary)