employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 75000},
    {"name": "Charlie", "salary": 62000},
    {"name": "Diana", "salary": 81000},
    {"name": "Evan", "salary": 45000}
]

def get_max_salary(employee_list):
    return max(emp["salary"] for emp in employee_list)

if __name__ == "__main__":
    result = get_max_salary(employees)
    print(result)