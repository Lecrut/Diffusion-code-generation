import json

def parse_employees(data):
    try:
        employees = json.loads(data)
    except json.JSONDecodeError:
        return 0
    
    max_salary = None
    
    for employee in employees:
        salary = employee.get("salary")
        if isinstance(salary, (int, float)):
            if max_salary is None or salary > max_salary:
                max_salary = salary
    
    return max_salary if max_salary is not None else 0

if __name__ == "__main__":
    sample_json = '[{"name": "Alice", "salary": 75000}, {"name": "Bob", "salary": "invalid"}, {"name": "Charlie", "salary": 82000}, {"name": "Diana", "salary": 68000.5}, {"name": "Eve", "salary": null}]'
    result = parse_employees(sample_json)
    print(result)