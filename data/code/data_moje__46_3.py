def get_max_salary(records):
    salaries = map(lambda r: r.get('salary') if isinstance(r.get('salary'), (int, float)) else None, records)
    valid_salaries = [s for s in salaries if s is not None]
    return max(valid_salaries) if valid_salaries else None

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 90000},
        {'name': 'Bob', 'salary': 'N/A'},
        {'name': 'Charlie', 'salary': 120000},
        {'name': 'Diana', 'salary': None},
        {'name': 'Eve', 'salary': 85000}
    ]
    print(get_max_salary(employees))