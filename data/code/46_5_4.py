def find_max_salary(salary_strings):
    return max(float(s.strip().replace(',', '')) for s in salary_strings if s.strip())

if __name__ == '__main__':
    sample_salaries = [
        "120,500.00",
        "95,750.25",
        "210,000.50",
        "85,000.00",
        "150,250.75",
        "  99,999.99  ",
        "250,000.00",
        "110,000.00"
    ]
    max_sal = find_max_salary(sample_salaries)
    print(max_sal)