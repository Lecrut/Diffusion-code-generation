def get_max_salary(salary_strings):
    return max(float(s) for s in salary_strings)

if __name__ == '__main__':
    salaries = ['50000.0', '75000.5', '120000.0', '90000.25', '60000.0']
    result = get_max_salary(salaries)
    print(result)