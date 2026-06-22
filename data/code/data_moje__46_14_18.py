def find_max_salary(salaries):
    return max([salary for salary in salaries])

if __name__ == '__main__':
    salaries = [50000, 60000, 75000, 55000, 80000, 65000]
    result = find_max_salary(salaries)
    print(result)