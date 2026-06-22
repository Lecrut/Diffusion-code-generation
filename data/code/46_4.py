import json

def get_max_salary():
    data = '[{"name": "Alice", "salary": 50000}, {"name": "Bob", "salary": 75000}, {"name": "Charlie", "salary": "invalid"}, {"name": "Diana", "salary": 60000}]'
    employees = json.loads(data)
    salaries = [emp["salary"] for emp in employees if isinstance(emp["salary"], (int, float))]
    if not salaries:
        return None
    return max(salaries)

if __name__ == '__main__':
    print(get_max_salary())