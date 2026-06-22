import json

def find_max_valid_salary(employees_json_string):
    employees = json.loads(employees_json_string)
    valid_salaries = []
    for employee in employees:
        salary = employee.get("salary")
        if isinstance(salary, (int, float)) and not isinstance(salary, bool):
            valid_salaries.append(salary)
    if not valid_salaries:
        return None
    return max(valid_salaries)

if __name__ == '__main__':
    sample_data = '[{"name": "Alice", "salary": 75000}, {"name": "Bob", "salary": "invalid"}, {"name": "Charlie", "salary": 82000.5}, {"name": "Diana", "salary": null}, {"name": "Eve", "salary": 60000}]'
    result = find_max_valid_salary(sample_data)
    print(result)