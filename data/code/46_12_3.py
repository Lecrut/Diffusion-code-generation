def get_max_salary():
    salaries = [45000, 62000, 78000, 54000, 91000, 67000]
    yield max(salaries)

if __name__ == '__main__':
    for value in get_max_salary():
        print(value)