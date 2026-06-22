employees = [
    {"name": "Alice", "salary": 75000, "department": "HR"},
    {"name": "Bob", "salary": 92000, "department": "Engineering"},
    {"name": "Charlie", "salary": "invalid", "department": "Marketing"},
    {"name": "Diana", "salary": 88000, "department": "Engineering"},
    {"name": "Eve", "salary": 65000, "department": "Sales"}
]
max_salary = max(map(lambda x: x["salary"] if isinstance(x.get("salary"), (int, float)) else float('-inf'), employees))
if __name__ == '__main__':
    print(max_salary)