import json

def compute_max_salary(json_string):
    data = json.loads(json_string)
    max_salary = None
    for employee in data:
        salary = employee.get('salary')
        if isinstance(salary, (int, float)) and not isinstance(salary, bool):
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_json = '[{"name": "Alice", "salary": 75000}, {"name": "Bob", "salary": "invalid"}, {"name": "Charlie", "salary": 85000.5}, {"name": "David", "salary": -5000}]'
    result = compute_max_salary(sample_json)
    print(result)