max_salary = lambda records: max(map(lambda r: r['salary'] if isinstance(r.get('salary'), (int, float)) else -float('inf'), records)) if any(isinstance(r.get('salary'), (int, float)) for r in records) else None
if __name__ == '__main__':
    employees = [{'name': 'Alice', 'salary': 50000}, {'name': 'Bob', 'salary': 'N/A'}, {'name': 'Charlie', 'salary': 75000.50}]
    print(max_salary(employees))