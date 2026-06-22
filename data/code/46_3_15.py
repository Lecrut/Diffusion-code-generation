def max_salary(records):
    return max(map(lambda r: r['salary'] if isinstance(r.get('salary'), (int, float)) else 0, records))

if __name__ == '__main__':
    sample_records = [
        {'name': 'Alice', 'salary': 95000},
        {'name': 'Bob', 'salary': 'high'},
        {'name': 'Charlie', 'salary': 120000},
        {'name': 'Diana', 'salary': 85000.5},
        {'name': 'Eve', 'salary': None}
    ]
    print(max_salary(sample_records))