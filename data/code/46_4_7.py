import json

def compute_max_salary(json_string):
    employees = json.loads(json_string)
    valid_salaries = []
    for employee in employees:
        salary = employee.get('salary')
        if salary is not None and isinstance(salary, (int, float)):
            valid_salaries.append(salary)
    if not valid_salaries:
        return None
    return max(valid_salaries)

if __name__ == '__main__':
    sample_json = '[{"name": "Alice", "salary": 85000}, {"name": "Bob", "salary": "invalid"}, {"name": "Charlie", "salary": 92000}, {"name": "David", "salary": 78000}]'
    result = compute_max_salary(sample_json)
    print(result)