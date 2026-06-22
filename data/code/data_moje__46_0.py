def find_max_salary(employees):
    if not employees:
        return None
    return max(employee['salary'] for employee in employees)

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 82000},
        {'name': 'Charlie', 'salary': 68000},
        {'name': 'Diana', 'salary': 91000}
    ]
    max_salary = find_max_salary(employees)
    print(max_salary)