def find_max_salary(salaries):
    return max([s for s in salaries])

if __name__ == '__main__':
    salaries = [45000, 60000, 72000, 55000, 80000]
    print(find_max_salary(salaries))