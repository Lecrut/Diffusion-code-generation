def get_max_salary(employees):
    if not employees:
        return None
    max_salary = max(emp.get('salary', 0) for emp in employees if isinstance(emp, dict))
    return max_salary

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 82000},
        {'name': 'Charlie', 'salary': 95000},
        {'name': 'David', 'salary': 67000}
    ]
    result = get_max_salary(sample_data)
    print(result)