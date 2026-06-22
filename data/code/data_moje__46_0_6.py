def find_max_salary(employees):
    return max(employee["salary"] for employee in employees)

if __name__ == "__main__":
    employees = [
        {"name": "Alice", "salary": 50000},
        {"name": "Bob", "salary": 75000},
        {"name": "Charlie", "salary": 65000},
        {"name": "Diana", "salary": 90000}
    ]
    result = find_max_salary(employees)
    print(result)