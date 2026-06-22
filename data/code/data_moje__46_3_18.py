def get_max_salary(records):
    return max(map(lambda r: float(r['salary']) if isinstance(r.get('salary'), (int, float, str)) and str(r['salary']).replace('.', '', 1).lstrip('-').isdigit() else 0.0, records))

if __name__ == '__main__':
    sample_records = [{'name': 'Alice', 'salary': 95000}, {'name': 'Bob', 'salary': '102000'}, {'name': 'Charlie', 'salary': 88000}, {'name': 'Dave', 'salary': 'invalid'}, {'name': 'Eve', 'salary': 105000.5}]
    print(get_max_salary(sample_records))