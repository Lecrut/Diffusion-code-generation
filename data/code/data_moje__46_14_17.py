def find_largest_salary(salaries):
    return max(salary for salary in salaries if isinstance(salary, (int, float)))

if __name__ == '__main__':
    salaries = [50000, 60000, 75000, 80000, 70000]
    result = find_largest_salary(salaries)
    print(result)