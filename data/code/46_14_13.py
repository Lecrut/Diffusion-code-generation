def find_max_salary(salaries):
    return max([s for s in salaries])

if __name__ == '__main__':
    salaries = [55000, 62000, 78500, 45000, 91000, 67000, 83000]
    result = find_max_salary(salaries)
    print(result)