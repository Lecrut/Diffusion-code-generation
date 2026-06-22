def generate_max_salary():
    salaries = [45000, 52000, 68000, 49000, 75000, 82000, 39000, 91000]
    for salary in salaries:
        yield salary
    yield max(salaries)

if __name__ == '__main__':
    values = list(generate_max_salary())
    print(values[-1])