def max_salary(salaries):
    return max(float(s) for s in salaries)

if __name__ == '__main__':
    salary_strings = ["50000.00", "60000.50", "75000.00", "80000.25", "45000.00"]
    result = max_salary(salary_strings)
    print(result)