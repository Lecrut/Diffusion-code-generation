def find_max_salary(salaries):
    return max([s for s in salaries])

if __name__ == '__main__':
    salaries = [55000, 72000, 68000, 91000, 84000]
    print(find_max_salary(salaries))