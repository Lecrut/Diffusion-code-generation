import operator
employee_data = [
    {"name": "Alice", "department": "HR", "salary": 60000},
    {"name": "Bob", "department": "Engineering", "salary": 85000},
    {"name": "Charlie", "department": "HR", "salary": 75000},
    {"name": "David", "department": "Engineering", "salary": 95000},
    {"name": "Eve", "department": "Sales", "salary": 65000},
    {"name": "Frank", "department": "Engineering", "salary": 85000},
    {"name": "Grace", "department": "HR", "salary": 55000}
]
def sort_employees(data):
    grouped_data = {}
    for employee in data:
        department = employee["department"]
        if department not in grouped_data:
            grouped_data[department] = []
        grouped_data[department].append(employee)
    sorted_data = {}
    for department, employees in grouped_data.items():
        sorted_salaries = sorted(employees, key=operator.itemgetter("salary"), reverse=True)
        sorted_data[department] = sorted_salaries
    return sorted_data
if __name__ == '__main__':
    sorted_employee_records = sort_employees(employee_data)
    print(sorted_employee_records)