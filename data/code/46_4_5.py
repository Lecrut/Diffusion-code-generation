import json

def parse_and_find_max_salary(json_string):
    data = json.loads(json_string)
    max_salary = None
    for employee in data:
        salary = employee.get('salary')
        if isinstance(salary, (int, float)) and not isinstance(salary, bool):
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_json = '[{"name": "Alice", "salary": 95000}, {"name": "Bob", "salary": "invalid"}, {"name": "Charlie", "salary": 120000.50}, {"name": "Diana", "salary": null}]'
    result = parse_and_find_max_salary(sample_json)
    print(result)