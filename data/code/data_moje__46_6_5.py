SALARY_DATA = [50000, 60000, 75000, 80000, 95000, 120000, 45000]

def get_max_salary(salary_list):
    if not salary_list:
        return None
    max_salary = salary_list[0]
    for salary in salary_list[1:]:
        if salary > max_salary:
            max_salary = salary
    return max_salary

if __name__ == '__main__':
    maximum = get_max_salary(SALARY_DATA)
    print(maximum)