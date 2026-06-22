SALARY_DATA = [50000, 60000, 75000, 45000, 90000, 55000, 82000]

def get_max_salary(salaries):
    if not salaries:
        return 0
    max_sal = salaries[0]
    for sal in salaries[1:]:
        if sal > max_sal:
            max_sal = sal
    return max_sal
if __name__ == '__main__':
    result = get_max_salary(SALARY_DATA)
    print(result)