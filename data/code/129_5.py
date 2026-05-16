import operator
def sort_employee_records(employees):
    grouped_by_department = {}
    for employee in employees:
        department = employee['department']
        if department not in grouped_by_department:
            grouped_by_department[department] = []
        grouped_by_department[department].append(employee)
    sorted_employees = {}
    for department, dept_employees in grouped_by_department.items():
        sorted_salaries = sorted(dept_employees, key=operator.itemgetter('salary'), reverse=True)
        sorted_employees[department] = sorted_salaries
    return sorted_employees
if __name__ == '__main__':
    employee_data = [
        {'name': 'Alice', 'department': 'HR', 'salary': 60000},
        {'name': 'Bob', 'department': 'Engineering', 'salary': 95000},
        {'name': 'Charlie', 'department': 'HR', 'salary': 75000},
        {'name': 'David', 'department': 'Engineering', 'salary': 110000},
        {'name': 'Eve', 'department': 'Sales', 'salary': 80000},
        {'name': 'Frank', 'department': 'Engineering', 'salary': 105000}
    ]
    sorted_data = sort_employee_records(employee_data)
    for department, employees in sorted_data.items():
        print(f"Department: {department}")
        for employee in employees:
            print(f"  Name: {employee['name']}, Salary: {employee['salary']}")
        print("-" * 20)