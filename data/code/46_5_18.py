def max_salary():
    salaries = [
        "50000.50",
        "60000.75",
        "45000.00",
        "75000.25",
        "55000.10",
        "80000.00",
        "42000.50",
        "90000.00",
        "35000.00",
        "65000.50"
    ]
    return max(float(s) for s in salaries)

if __name__ == '__main__':
    result = max_salary()
    print(result)