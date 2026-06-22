from typing import ClassVar

class LeapYearChecker:
    def is_leap_year(self, year: int) -> bool:
        if year % 4 != 0:
            return False
        if year % 100 != 0:
            return True
        return year % 400 == 0

if __name__ == '__main__':
    checker = LeapYearChecker()
    test_years = [2000, 1900, 2024, 2023, 2400, 2100]
    for year in test_years:
        result = checker.is_leap_year(year)
        print(f"{year}: {result}")