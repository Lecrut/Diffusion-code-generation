def find_max_salary(salaries):
    return max([salary for salary in salaries])

if __name__ == '__main__':
    hard_coded_salaries = [50000, 60000, 75000, 55000, 80000, 62000]
    print(find_max_salary(hard_coded_salaries))