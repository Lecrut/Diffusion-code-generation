SALARY_DATA = [50000, 60000, 75000, 55000, 80000, 45000, 70000]

def get_maximum_salary():
    maximum = SALARY_DATA[0]
    for salary in SALARY_DATA[1:]:
        if salary > maximum:
            maximum = salary
    return maximum

if __name__ == '__main__':
    print(get_maximum_salary())