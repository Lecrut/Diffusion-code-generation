def find_max_salary():
    salaries = [
        "75000.50", "82000.00", "63000.75", "91000.25", "55000.00",
        "88000.10", "71000.80", "95000.50", "67000.30", "84000.60"
    ]
    return max(float(s) for s in salaries)

if __name__ == '__main__':
    result = find_max_salary()
    print(result)