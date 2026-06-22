SALARY_DATA = [50000, 60000, 75000, 45000, 80000, 55000, 90000]

def get_max_salary(salaries):
    if not salaries:
        return None
    max_salary = salaries[0]
    for salary in salaries[1:]:
        if salary > max_salary:
            max_salary = salary
    return max_salary
if __name__ == '__main__':
    result = get_max_salary(SALARY_DATA)
    print(result)