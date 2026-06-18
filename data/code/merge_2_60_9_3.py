def is_leap_year(year: int) -> bool:
    if year < 0:
        return False
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    test_cases = [2000, 2023, 1900, -5]
    for case in test_cases:
        result = is_leap_year(case)
        print(f"{case}: {result}")