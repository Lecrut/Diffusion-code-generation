def find_max_salary(salaries):
    return max([s for s in salaries if isinstance(s, (int, float))])

if __name__ == '__main__':
    salaries = [50000, 60000, 75000, 45000, 80000]
    result = find_max_salary(salaries)
    print(result)