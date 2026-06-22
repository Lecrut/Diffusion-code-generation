SALARY_DATA = [50000, 60000, 75000, 55000, 80000, 65000, 70000]

def get_maximum_salary(salaries):
    if not salaries:
        raise ValueError('Salary list cannot be empty')
    max_salary = salaries[0]
    for salary in salaries[1:]:
        if salary > max_salary:
            max_salary = salary
    return max_salary
if __name__ == '__main__':
    result = get_maximum_salary(SALARY_DATA)
    print(result)