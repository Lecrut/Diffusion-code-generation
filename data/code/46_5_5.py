def find_max_salary(salary_strings):
    return max(float(salary) for salary in salary_strings)

if __name__ == '__main__':
    sample_salaries = ["50000.50", "75000.25", "62000.00", "91000.75", "48000.10"]
    result = find_max_salary(sample_salaries)
    print(result)