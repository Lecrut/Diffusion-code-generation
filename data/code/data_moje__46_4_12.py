import json

def find_max_salary(employees_json):
    employees = json.loads(employees_json)
    max_salary = None
    for employee in employees:
        salary = employee.get('salary')
        if isinstance(salary, (int, float)):
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_json = '''
    [
        {"name": "Alice", "salary": 75000},
        {"name": "Bob", "salary": "invalid"},
        {"name": "Charlie", "salary": 95000},
        {"name": "Diana", "salary": 82000.5}
    ]
    '''
    result = find_max_salary(sample_json)
    print(result)