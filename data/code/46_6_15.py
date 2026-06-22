SALARIES = [50000, 60000, 75000, 82000, 95000, 110000, 48000]

def get_max_salary(salary_list):
    max_salary = salary_list[0]
    for salary in salary_list[1:]:
        if salary > max_salary:
            max_salary = salary
    return max_salary

if __name__ == '__main__':
    result = get_max_salary(SALARIES)
    print(result)