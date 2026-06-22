def find_max_salary():
    salaries = [50000, 75000, 62000, 90000, 55000, 88000]
    return max([s for s in salaries])

if __name__ == '__main__':
    result = find_max_salary()
    print(result)