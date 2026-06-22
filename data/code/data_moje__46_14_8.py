def find_max_salary(salaries):
    return max(salaries)

if __name__ == '__main__':
    salary_data = [50000, 120000, 95000, 75000, 200000]
    highest_salary = find_max_salary(salary_data)
    print(highest_salary)