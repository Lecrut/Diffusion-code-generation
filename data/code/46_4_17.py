import json
import sys

def find_max_valid_salary(employees_json):
    try:
        data = json.loads(employees_json)
    except json.JSONDecodeError:
        return None
    
    max_salary = None
    
    for employee in data:
        salary = employee.get("salary")
        if isinstance(salary, (int, float)) and not isinstance(salary, bool):
            if max_salary is None or salary > max_salary:
                max_salary = salary
    
    return max_salary

if __name__ == '__main__':
    sample_json = '''
    [
        {"name": "Alice", "salary": 75000},
        {"name": "Bob", "salary": "invalid"},
        {"name": "Charlie", "salary": 82000},
        {"name": "Diana", "salary": null},
        {"name": "Eve", "salary": 65000.50}
    ]
    '''
    result = find_max_valid_salary(sample_json)
    print(result)