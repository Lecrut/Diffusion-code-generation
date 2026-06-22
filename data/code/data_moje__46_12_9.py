def max_salary_generator():
    salaries = [50000, 75000, 45000, 90000, 60000, 110000, 85000]
    yield max(salaries)

if __name__ == '__main__':
    for value in max_salary_generator():
        print(value)