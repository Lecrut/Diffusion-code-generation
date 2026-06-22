def find_max_salary(salary_strings):
    return max(float(s) for s in salary_strings)

if __name__ == '__main__':
    salaries = ["50000.50", "75000.25", "60000.00", "95000.75", "45000.10"]
    result = find_max_salary(salaries)
    print(result)