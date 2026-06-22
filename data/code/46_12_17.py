def max_salary_generator():
    salaries = [50000, 60000, 55000, 70000, 65000, 75000, 80000, 72000, 68000, 85000]
    for salary in salaries:
        yield salary

if __name__ == '__main__':
    generator = max_salary_generator()
    result = max(generator)
    print(result)