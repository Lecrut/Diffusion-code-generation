def max_salary_generator():
    salaries = [50000, 60000, 75000, 45000, 82000, 55000, 91000, 48000, 67000, 73000]
    yield max(salaries)

if __name__ == '__main__':
    generator = max_salary_generator()
    result = next(generator)
    print(result)