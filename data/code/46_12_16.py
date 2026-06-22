def max_salary_generator(salaries):
    for salary in salaries:
        yield salary
    if salaries:
        yield max(salaries)

if __name__ == '__main__':
    sample_salaries = [50000, 60000, 45000, 75000, 82000]
    result = None
    for value in max_salary_generator(sample_salaries):
        result = value
    print(result)