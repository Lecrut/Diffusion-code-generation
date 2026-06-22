def max_salary(records):
    return max(map(lambda r: float(r['salary']) if isinstance(r.get('salary'), (int, float)) else -float('inf'), records))

if __name__ == '__main__':
    sample_records = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 'unknown'},
        {'name': 'Charlie', 'salary': 82000},
        {'name': 'Diana', 'salary': 65000.5},
        {'name': 'Eve', 'salary': None}
    ]
    print(max_salary(sample_records))