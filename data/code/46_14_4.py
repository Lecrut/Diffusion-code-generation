def find_max_salary(salaries):
    return max([salary for salary in salaries if isinstance(salary, (int, float))])

if __name__ == '__main__':
    salaries = [50000, 75000, 120000, 90000, 65000, 'N/A', 80000]
    result = find_max_salary(salaries)
    print(result)