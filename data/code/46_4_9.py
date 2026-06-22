import json

def parse_employees_and_find_max_salary(json_str):
    employees = json.loads(json_str)
    valid_salaries = []
    for employee in employees:
        salary = employee.get('salary')
        if isinstance(salary, (int, float)) and not isinstance(salary, bool):
            valid_salaries.append(salary)
    if not valid_salaries:
        return None
    return max(valid_salaries)

if __name__ == '__main__':
    sample_json = '''
    [
        {"name": "Alice", "salary": 75000, "department": "Engineering"},
        {"name": "Bob", "salary": "not_a_number", "department": "Marketing"},
        {"name": "Charlie", "salary": 95000.50, "department": "Engineering"},
        {"name": "Diana", "salary": 60000, "department": "HR"},
        {"name": "Eve", "salary": null, "department": "Sales"},
        {"name": "Frank", "salary": 120000, "department": "Engineering"}
    ]
    '''
    result = parse_employees_and_find_max_salary(sample_json)
    print(result)