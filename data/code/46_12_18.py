def get_max_salary(salaries):
    max_val = max(salaries)
    yield max_val

if __name__ == '__main__':
    hard_coded_salaries = [50000, 60000, 75000, 80000, 55000]
    result = next(get_max_salary(hard_coded_salaries))
    print(result)