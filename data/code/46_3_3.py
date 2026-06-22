max_salary = lambda records: max(map(lambda r: float(r['salary']) if isinstance(r.get('salary'), (int, float)) else -1, records)) if records else 0

if __name__ == '__main__':
    employees = [{'name': 'Alice', 'salary': 50000}, {'name': 'Bob', 'salary': 'invalid'}, {'name': 'Charlie', 'salary': 75000}]
    print(max_salary(employees))