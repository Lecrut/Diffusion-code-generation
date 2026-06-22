def get_max_salary(employees):
    return max(
        (emp['salary'] for emp in employees),
        default=0
    )

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 85000},
        {'name': 'Charlie', 'salary': 72000}
    ]

    result = get_max_salary(sample_data)
    print(result)