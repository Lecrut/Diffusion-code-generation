from typing import Union

class LeapYearVerifier:
    def is_leap_year(self, year: int) -> bool:
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

if __name__ == '__main__':
    verifier = LeapYearVerifier()
    test_years = [2000, 1900, 2024, 2023, 1996, 2100]
    for year in test_years:
        result = verifier.is_leap_year(year)
        print(f"{year}: {result}")