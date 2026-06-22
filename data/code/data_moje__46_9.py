def find_max_salary(nested_departments):
    max_salary = float('-inf')
    for department in nested_departments:
        if isinstance(department, list):
            for employee in department:
                if isinstance(employee, list):
                    for salary in employee:
                        if isinstance(salary, (int, float)):
                            if salary > max_salary:
                                max_salary = salary
                elif isinstance(employee, (int, float)):
                    if employee > max_salary:
                        max_salary = employee
        elif isinstance(department, (int, float)):
            if department > max_salary:
                max_salary = department
    return max_salary

if __name__ == '__main__':
    departments = [
        [3500, 4200, 3800],
        [4500, [5000, 4100], 4800],
        [3900, 5200, [5100, 4900]]
    ]
    print(find_max_salary(departments))