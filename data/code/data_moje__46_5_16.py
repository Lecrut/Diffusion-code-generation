def get_max_salary():
    salaries = [
        "45000.00",
        "120000.50",
        "67500.75",
        "98000.00",
        "150000.25",
        "32000.00",
        "75000.50",
        "210000.00",
        "55000.75",
        "180000.00"
    ]
    return max(float(s) for s in salaries)

if __name__ == '__main__':
    result = get_max_salary()
    print(result)