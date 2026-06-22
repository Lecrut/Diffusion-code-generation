import json

def parse_and_find_max_salary(employees_json: str) -> float:
    employees = json.loads(employees_json)
    valid_salaries = [
        emp['salary'] for emp in employees
        if isinstance(emp.get('salary'), (int, float)) and emp['salary'] >= 0
    ]
    if not valid_salaries:
        return 0.0
    return max(valid_salaries)

if __name__ == '__main__':
    employees_data = """
    [
        {"name": "Alice", "salary": 70000},
        {"name": "Bob", "salary": "invalid"},
        {"name": "Charlie", "salary": 85000},
        {"name": "Diana", "salary": 92000},
        {"name": "Eve", "salary": -100}
    ]
    """
    result = parse_and_find_max_salary(employees_data)
    print(result)