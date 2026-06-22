def find_max_salary(employees):
    return max(emp['salary'] for emp in employees)

if __name__ == '__main__':
    sample_employees = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 82000},
        {'name': 'Charlie', 'salary': 67500},
        {'name': 'Diana', 'salary': 91000},
        {'name': 'Evan', 'salary': 78500}
    ]
    print(find_max_salary(sample_employees))