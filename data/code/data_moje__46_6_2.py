SALARY_DATA = [45000, 62000, 53000, 71000, 59000, 48000, 67000, 82000, 55000, 76000]

def get_max_salary(salary_list):
    if not salary_list:
        return 0
    max_salary = salary_list[0]
    for salary in salary_list:
        if salary > max_salary:
            max_salary = salary
    return max_salary

if __name__ == '__main__':
    max_value = get_max_salary(SALARY_DATA)
    print(max_value)