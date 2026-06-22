import json

def compute_max_valid_salary(json_data):
    data = json.loads(json_data)
    max_salary = None
    for employee in data:
        salary = employee.get('salary')
        if salary is not None and isinstance(salary, (int, float)) and not isinstance(salary, bool):
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_json = json.dumps([
        {"name": "Alice", "salary": 75000},
        {"name": "Bob", "salary": "invalid"},
        {"name": "Charlie", "salary": 85000},
        {"name": "Diana", "salary": None},
        {"name": "Eve", "salary": 92000}
    ])
    result = compute_max_valid_salary(sample_json)
    print(result)