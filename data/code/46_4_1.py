import json

def find_max_valid_salary(json_str):
    data = json.loads(json_str)
    max_salary = None
    for employee in data:
        salary = employee.get("salary")
        if salary is not None and isinstance(salary, (int, float)):
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_json = '[{"name": "Alice", "salary": 85000}, {"name": "Bob", "salary": "invalid"}, {"name": "Charlie", "salary": 92000}, {"name": "Diana", "salary": 78000}]'
    result = find_max_valid_salary(sample_json)
    print(result)