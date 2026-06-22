employees = [
    {"name": "Alice", "salary": 70000},
    {"name": "Bob", "salary": 85000},
    {"name": "Charlie", "salary": 60000},
    {"name": "Diana", "salary": 95000}
]

def find_max_salary(data):
    return max(emp["salary"] for emp in data)

if __name__ == '__main__':
    print(find_max_salary(employees))