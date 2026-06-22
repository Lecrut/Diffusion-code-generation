employees = [{'name': 'Alice', 'salary': 75000}, {'name': 'Bob', 'salary': 82000}, {'name': 'Charlie', 'salary': 'unknown'}, {'name': 'Diana', 'salary': 68000}]
max_salary = lambda records: max(map(lambda r: float(r['salary']) if isinstance(r.get('salary'), (int, float)) else -1, records))
if __name__ == '__main__':
    print(max_salary(employees))