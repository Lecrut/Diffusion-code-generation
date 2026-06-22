def find_max_salary(salary_strings):
    return max(float(s) for s in salary_strings)

if __name__ == '__main__':
    salaries = ["50000.00", "75250.50", "120000.75", "30000.25", "98500.00"]
    result = find_max_salary(salaries)
    print(result)