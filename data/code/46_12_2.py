def generate_max_salary():
    salaries = [45000, 52000, 78000, 63000, 91000, 55000, 82000]
    max_salary = max(salaries)
    yield max_salary

if __name__ == '__main__':
    for value in generate_max_salary():
        print(value)