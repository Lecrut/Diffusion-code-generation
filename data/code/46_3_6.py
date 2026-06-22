import math

def get_max_salary(employees):
    return max(
        map(
            lambda record: float(record.get('salary', 0)) if isinstance(record.get('salary'), (int, float)) and not isinstance(record.get('salary'), bool) else 0,
            employees
        )
    )

if __name__ == '__main__':
    sample_employees = [
        {'name': 'Alice', 'salary': 50000},
        {'name': 'Bob', 'salary': 75000.5},
        {'name': 'Charlie', 'salary': 'invalid'},
        {'name': 'Diana', 'salary': None},
        {'name': 'Eve', 'salary': 60000}
    ]
    result = get_max_salary(sample_employees)
    print(result)