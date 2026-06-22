def find_max_salary(salaries):
    return max([salary for salary in salaries])

if __name__ == '__main__':
    salary_figures = [50000, 65000, 72000, 58000, 89000, 45000]
    print(find_max_salary(salary_figures))