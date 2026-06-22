def get_max_salary():
    salary_strings = [
        "50000.50", "60000.00", "75000.25", "45000.75", "90000.00",
        "120000.50", "85000.00", "95000.25", "110000.00", "65000.50",
        "70000.00", "80000.75", "55000.00", "92000.50", "88000.00",
        "67000.25", "73000.00", "99000.50", "105000.00", "62000.75"
    ]
    max_sal = max(float(s) for s in salary_strings)
    return max_sal

if __name__ == '__main__':
    result = get_max_salary()
    print(result)