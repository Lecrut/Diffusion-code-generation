def max_salary(records):
    return max(map(lambda rec: rec.get('salary', 0) if isinstance(rec, dict) and isinstance(rec.get('salary'), (int, float)) else 0, records))

if __name__ == '__main__':
    sample_records = [
        {'name': 'Alice', 'salary': 75000},
        {'name': 'Bob', 'salary': 'unknown'},
        {'name': 'Charlie', 'salary': 82000},
        {'name': 'Diana', 'salary': 95000},
        'invalid_entry',
        {'name': 'Eve', 'salary': -1}
    ]
    print(max_salary(sample_records))