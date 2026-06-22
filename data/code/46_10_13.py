def get_max_salary(employees):
    if not employees:
        return None
    max_sal = max(emp.get('salary', 0) for emp in employees)
    return max_sal

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 120000},
        {'name': 'Charlie', 'salary': 110000}
    ]
    print(get_max_salary(sample_data))