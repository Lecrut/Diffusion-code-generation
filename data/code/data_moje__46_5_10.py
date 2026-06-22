def find_max_salary(salary_strings):
    return max(float(s) for s in salary_strings)

if __name__ == '__main__':
    salaries = ["50000.00", "120000.50", "75000.25", "95000.00", "200000.00"]
    result = find_max_salary(salaries)
    print(result)