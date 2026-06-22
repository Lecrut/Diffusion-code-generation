def max_salary_generator():
    salaries = [50000, 60000, 75000, 80000, 95000, 120000, 110000]
    yield max(salaries)

if __name__ == '__main__':
    result = list(max_salary_generator())
    print(result[0])