def max_salary_generator():
    salaries = [50000, 60000, 75000, 80000, 65000, 90000, 55000]
    yield max(salaries)

if __name__ == '__main__':
    print(next(max_salary_generator()))