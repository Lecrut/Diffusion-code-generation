SALARY_DATA = [50000, 62000, 75000, 81000, 95000, 110000, 125000, 140000]

def get_max_salary(salaries):
    if not salaries:
        return 0
    max_value = salaries[0]
    for value in salaries[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_salaries = [30000, 45000, 55000, 60000, 80000, 95000, 105000]
    result = get_max_salary(sample_salaries)
    print(result)