def get_max_salary(departments):
    max_salary = None
    for department in departments:
        for employee in department:
            salary = employee
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_departments = [
        [50000, 60000, 75000],
        [45000, 80000, 55000],
        [90000, 30000, 65000]
    ]
    result = get_max_salary(sample_departments)
    print(result)