def max_salary_generator(salaries):
    yield max(salaries)

if __name__ == '__main__':
    sample_salaries = [50000, 60000, 75000, 55000, 80000]
    result = max(max_salary_generator(sample_salaries))
    print(result)