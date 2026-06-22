def get_max_salary(salaries):
    if not salaries:
        return None
    max_salary = salaries[0]
    for salary in salaries[1:]:
        if salary > max_salary:
            max_salary = salary
    return max_salary

if __name__ == '__main__':
    sample_salaries = [50000, 120000, 75000, 95000, 110000]
    result = get_max_salary(sample_salaries)
    print(result)