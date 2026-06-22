def get_max_salary():
    salaries = [
        "50000.00",
        "120000.50",
        "75000.25",
        "95000.00",
        "60000.75",
        "150000.00",
        "85000.50",
        "45000.25",
        "110000.00",
        "70000.00"
    ]
    max_salary = max(float(s) for s in salaries)
    return max_salary

if __name__ == '__main__':
    result = get_max_salary()
    print(result)