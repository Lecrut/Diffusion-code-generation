def find_max_salary():
    salary_strings = [
        "75000.50", "82000.75", "91000.00", "65000.25", "105000.00",
        "88500.50", "95000.75", "72000.00", "110000.50", "68000.25",
        "99000.00", "84000.50", "102000.75", "77000.00", "93000.50",
        "81000.25", "97000.00", "70000.50", "108000.75", "62000.00"
    ]
    max_salary = max(float(s) for s in salary_strings)
    return max_salary

if __name__ == '__main__':
    result = find_max_salary()
    print(result)