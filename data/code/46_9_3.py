def find_max_salary(departments):
    max_salary = None
    for department in departments:
        for employee_data in department:
            if isinstance(employee_data, (int, float)):
                if max_salary is None or employee_data > max_salary:
                    max_salary = employee_data
            elif isinstance(employee_data, list):
                nested_max = find_max_salary([employee_data])
                if nested_max is not None and (max_salary is None or nested_max > max_salary):
                    max_salary = nested_max
    return max_salary

if __name__ == '__main__':
    data = [
        [100, 200, [300, 400]],
        [500, [600, [700]]],
        [800, 900]
    ]
    print(find_max_salary(data))