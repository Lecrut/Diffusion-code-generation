import json

def get_max_salary(employees):
    valid_salaries = [
        emp['salary']
        for emp in employees
        if isinstance(emp.get('salary'), (int, float)) and emp['salary'] >= 0
    ]
    if not valid_salaries:
        return 0
    return max(valid_salaries)

if __name__ == '__main__':
    data = '[{"name": "Alice", "salary": 75000}, {"name": "Bob", "salary": "N/A"}, {"name": "Charlie", "salary": 82000}, {"name": "Diana", "salary": null}, {"name": "Eve", "salary": 65000}]'
    employees = json.loads(data)
    max_sal = get_max_salary(employees)
    print(max_sal)