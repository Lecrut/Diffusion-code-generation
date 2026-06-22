def max_salary_from_strings(salary_strings):
    return max((float(salary.strip().replace(',', '')) for salary in salary_strings))

if __name__ == '__main__':
    sample_salaries = [
        "50,000.00",
        "75,500.50",
        "60,250.75",
        "90,000.00",
        "45,000.25",
        "1,200,000.00",
        "300,000.99"
    ]
    result = max_salary_from_strings(sample_salaries)
    print(result)