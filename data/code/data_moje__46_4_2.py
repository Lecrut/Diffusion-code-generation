import json

def get_max_salary(employees):
    salaries = [emp['salary'] for emp in employees if isinstance(emp.get('salary'), (int, float))]
    return max(salaries) if salaries else None

if __name__ == '__main__':
    data = '''[
        {"name": "Alice", "age": 30, "salary": 75000},
        {"name": "Bob", "age": 25, "salary": "invalid"},
        {"name": "Charlie", "age": 35, "salary": 92000},
        {"name": "Diana", "age": 28},
        {"name": "Eve", "age": 32, "salary": 85000}
    ]'''
    employees_list = json.loads(data)
    print(get_max_salary(employees_list))