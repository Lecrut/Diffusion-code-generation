SALARY_DATA = [50000, 60000, 75000, 55000, 80000, 45000, 90000]

def get_maximum_salary(salaries):
    if not salaries:
        return None
    maximum = salaries[0]
    for salary in salaries[1:]:
        if salary > maximum:
            maximum = salary
    return maximum

if __name__ == '__main__':
    result = get_maximum_salary(SALARY_DATA)
    print(result)