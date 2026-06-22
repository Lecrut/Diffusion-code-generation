def get_max_salary(salary_list):
    return max(salary_list)

if __name__ == '__main__':
    salaries = [50000, 60000, 75000, 80000, 70000]
    print(get_max_salary(salaries))