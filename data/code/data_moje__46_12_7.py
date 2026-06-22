def yield_max_salary():
    salaries = [50000, 60000, 75000, 45000, 80000, 55000]
    yield max(salaries)

if __name__ == '__main__':
    print(list(yield_max_salary())[0])