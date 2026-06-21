def evaluate_leap_status(target_year):
    return target_year % 4 == 0 and (target_year % 100 != 0 or target_year % 400 == 0)

if __name__ == '__main__':
    test_cases = [1700, 2000, 2024, 2025, 2400]
    for year in test_cases:
        result = evaluate_leap_status(year)
        print(result)