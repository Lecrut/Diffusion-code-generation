import json

def get_max_salary(employees_json):
    employees = json.loads(employees_json)
    max_salary = None
    for emp in employees:
        salary = emp.get('salary')
        if isinstance(salary, (int, float)) and not isinstance(salary, bool):
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_json = '[{"name": "Alice", "salary": 75000}, {"name": "Bob", "salary": 85000}, {"name": "Charlie", "salary": "invalid"}, {"name": "Diana", "salary": 92000}]'
    result = get_max_salary(sample_json)
    print(result)