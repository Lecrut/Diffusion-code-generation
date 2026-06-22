def find_max_salary(employees):
    if not employees:
        return None
    return max(employee['salary'] for employee in employees)

if __name__ == '__main__':
    employee_list = [
        {'name': 'Alice', 'salary': 55000},
        {'name': 'Bob', 'salary': 72000},
        {'name': 'Charlie', 'salary': 63000},
        {'name': 'Diana', 'salary': 81000}
    ]
    max_val = find_max_salary(employee_list)
    print(max_val)