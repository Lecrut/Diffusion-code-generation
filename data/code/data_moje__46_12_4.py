def max_salary_generator():
    salaries = [45000, 60000, 75000, 55000, 90000, 82000, 65000, 71000, 88000, 50000]
    yield max(salaries)

if __name__ == '__main__':
    gen = max_salary_generator()
    print(next(gen))