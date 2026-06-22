def get_max_salary(salaries):
    return max(salaries)

if __name__ == '__main__':
    salaries = [50000, 60000, 75000, 55000, 80000]
    result = get_max_salary(salaries)
    print(result)