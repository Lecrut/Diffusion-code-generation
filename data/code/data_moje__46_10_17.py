def get_max_salary(employees):
    if not employees:
        return None
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    sample_employees = [
        {'name': 'Alice', 'salary': 85000},
        {'name': 'Bob', 'salary': 92000},
        {'name': 'Charlie', 'salary': 78000}
    ]
    print(get_max_salary(sample_employees))