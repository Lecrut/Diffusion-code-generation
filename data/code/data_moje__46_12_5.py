def max_salary_generator(salaries):
    max_salary = -float('inf')
    for salary in salaries:
        max_salary = max(max_salary, salary)
    yield max_salary

if __name__ == '__main__':
    salaries = [50000, 60000, 70000, 80000, 90000]
    result = next(max_salary_generator(salaries))
    print(result)