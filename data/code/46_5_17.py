def find_max_salary(salary_strings):
    if not salary_strings:
        return None
    return max(float(s) for s in salary_strings)

if __name__ == '__main__':
    salaries = ["50000.50", "75000.25", "99999.99", "60000.00", "85000.75"]
    result = find_max_salary(salaries)
    print(result)