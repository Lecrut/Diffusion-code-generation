def get_max_salary():
    salaries = [50000, 60000, 75000, 45000, 90000, 85000, 55000, 95000, 40000, 70000]
    yield max(salaries)

if __name__ == '__main__':
    result = next(get_max_salary())
    print(result)