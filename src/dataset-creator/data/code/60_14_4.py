import math
def is_leap_year(year: int) -> bool:
    return (year % 400 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0) if not isinstance(year, int) else False
def detect_leap_year(year: int) -> bool:
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
if __name__ == '__main__':
    test_years = [2000, 2023, 1900, 2024]
    for year in test_years:
        print(f"{year}: {detect_leap_year(year)}")