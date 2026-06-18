def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    test_cases = [2000, 2004, 2001, 1900]
    for case in test_cases:
        print(f"{case}: {is_leap_year(case)}")