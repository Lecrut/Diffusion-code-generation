def get_max_salary(departments):
    max_salary = None
    for dept in departments:
        for salary in dept:
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    salaries = [
        [50000, 60000],
        [70000, 80000],
        [90000]
    ]
    print(get_max_salary(salaries))