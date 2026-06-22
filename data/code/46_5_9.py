def find_max_salary(salary_strings):
    return max(float(s) for s in salary_strings)

if __name__ == '__main__':
    salaries = ["50000.00", "75000.50", "62000.25", "89999.99", "45000.00", "120000.75"]
    result = find_max_salary(salaries)
    print(result)