def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
if __name__ == '__main__':
    test_years = [1900, 2000, 2024, 2100, 2400]
    print("Leap Year Calculation Results:")
    print("-" * 30)
    for year in test_years:
        result = is_leap_year(year)
        status_str = "LEAP YEAR" if result else "COMMON YEAR"
        print(f"{year} {status_str}")