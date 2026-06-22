import json

def get_max_valid_salary(json_string):
    employees = json.loads(json_string)
    valid_salaries = []
    for emp in employees:
        salary = emp.get("salary")
        if isinstance(salary, (int, float)):
            if salary >= 0:
                valid_salaries.append(salary)
    if not valid_salaries:
        return None
    return max(valid_salaries)

if __name__ == '__main__':
    sample_json = '[{"name": "Alice", "salary": 50000}, {"name": "Bob", "salary": "invalid"}, {"name": "Charlie", "salary": 75000}, {"name": "Diana", "salary": -1000}, {"name": "Eve", "salary": 60000.5}]'
    result = get_max_valid_salary(sample_json)
    print(result)