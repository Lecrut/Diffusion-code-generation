import json

def find_max_salary(json_string):
    employees = json.loads(json_string)
    salaries = []
    for emp in employees:
        if 'salary' in emp and isinstance(emp['salary'], (int, float)):
            salaries.append(emp['salary'])
    if salaries:
        return max(salaries)
    return None

if __name__ == '__main__':
    sample_json = '''
    [
        {"name": "Alice", "salary": 50000},
        {"name": "Bob", "salary": "invalid"},
        {"name": "Charlie", "salary": 75000.5},
        {"name": "Diana", "salary": 60000},
        {"name": "Eve", "salary": -1000},
        {"name": "Frank", "salary": null}
    ]
    '''
    result = find_max_salary(sample_json)
    print(result)