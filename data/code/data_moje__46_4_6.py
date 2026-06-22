import json

def find_max_valid_salary(employee_data):
    max_salary = None
    for employee in employee_data:
        if "salary" in employee:
            try:
                salary_value = int(employee["salary"]) if isinstance(employee["salary"], str) else employee["salary"]
                if isinstance(salary_value, (int, float)):
                    if max_salary is None or salary_value > max_salary:
                        max_salary = salary_value
            except (ValueError, TypeError):
                continue
    return max_salary

if __name__ == '__main__':
    employees_json = '''
    [
        {"name": "Alice", "salary": 75000},
        {"name": "Bob", "salary": "invalid"},
        {"name": "Charlie", "salary": 82000},
        {"name": "Diana"},
        {"name": "Eve", "salary": 65000.50},
        {"name": "Frank", "salary": "90000"}
    ]
    '''
    employees = json.loads(employees_json)
    result = find_max_valid_salary(employees)
    print(result)