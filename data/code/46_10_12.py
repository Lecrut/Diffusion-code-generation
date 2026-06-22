def get_max_salary(data):
    max_salary = float('-inf')
    for employee in data:
        salary = employee.get("salary", 0)
        if salary > max_salary:
            max_salary = salary
    return max_salary if max_salary != float('-inf') else 0

if __name__ == '__main__':
    employees = [
        {"name": "Alice", "salary": 50000},
        {"name": "Bob", "salary": 75000},
        {"name": "Charlie", "salary": 60000}
    ]
    result = get_max_salary(employees)
    print(result)