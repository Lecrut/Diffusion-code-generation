def find_max_salary(salary_strings):
    return max(float(salary) for salary in salary_strings)

if __name__ == '__main__':
    salaries = ["50000.00", "75000.50", "120000.75", "45000.25", "90000.00"]
    print(find_max_salary(salaries))