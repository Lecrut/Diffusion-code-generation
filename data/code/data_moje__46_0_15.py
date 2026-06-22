def get_max_salary(employees):
    return max(employee["salary"] for employee in employees)

if __name__ == "__main__":
    employees = [
        {"name": "Alice", "salary": 75000},
        {"name": "Bob", "salary": 82000},
        {"name": "Charlie", "salary": 65000},
        {"name": "Diana", "salary": 91000}
    ]
    result = get_max_salary(employees)
    print(result)