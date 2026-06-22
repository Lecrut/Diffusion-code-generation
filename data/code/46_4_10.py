import json

def parse_and_find_max_salary(json_str):
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return None

    if not isinstance(data, list):
        return None

    valid_salaries = []
    for employee in data:
        if not isinstance(employee, dict):
            continue
        salary = employee.get('salary')
        if isinstance(salary, (int, float)) and not isinstance(salary, bool):
            valid_salaries.append(salary)

    if not valid_salaries:
        return None

    return max(valid_salaries)

if __name__ == '__main__':
    json_string = '[{"name": "Alice", "salary": 85000}, {"name": "Bob", "salary": "invalid"}, {"name": "Charlie", "salary": 92000}, {"name": "Diana", "salary": 78000}]'
    result = parse_and_find_max_salary(json_string)
    print(result)