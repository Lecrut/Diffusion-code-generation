def find_max_salary(departments):
    max_salary = None
    for department in departments:
        for salary in department:
            if max_salary is None or salary > max_salary:
                max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_departments = [
        [50000, 60000, 75000],
        [45000, 85000, 90000],
        [55000, 62000]
    ]
    print(find_max_salary(sample_departments))