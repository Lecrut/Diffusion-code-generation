def get_max_salary(employees):
    salaries = map(lambda e: e.get('salary') if isinstance(e.get('salary'), (int, float)) else None, employees)
    valid_salaries = filter(lambda s: s is not None, salaries)
    return max(valid_salaries) if valid_salaries else None

if __name__ == '__main__':
    employees = [{'name': 'Alice', 'salary': 100000}, {'name': 'Bob', 'salary': 'invalid'}, {'name': 'Charlie', 'salary': 120000}]
    result = get_max_salary(employees)
    print(result)