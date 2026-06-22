import json

def find_max_valid_salary(employee_data):
    valid_salaries = []
    for employee in employee_data:
        salary = employee.get("salary")
        if isinstance(salary, (int, float)) and salary > 0:
            valid_salaries.append(salary)
    
    if not valid_salaries:
        return None
    
    return max(valid_salaries)

if __name__ == '__main__':
    employees_json = """
    [
        {"name": "Alice", "salary": 75000, "department": "HR"},
        {"name": "Bob", "salary": "not_a_number", "department": "IT"},
        {"name": "Charlie", "salary": 92000, "department": "Engineering"},
        {"name": "Diana", "salary": -500, "department": "Sales"},
        {"name": "Eve", "salary": 88000.50, "department": "Marketing"},
        {"name": "Frank", "department": "Support"}
    ]
    """
    
    data = json.loads(employees_json)
    max_salary = find_max_valid_salary(data)
    print(max_salary)