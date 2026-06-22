def max_salary(salary_strings):
    return max(float(s) for s in salary_strings)

if __name__ == '__main__':
    salaries = ["45000.50", "52000.75", "48500.25", "60000.00", "51000.99", "47000.10"]
    print(max_salary(salaries))