from typing import Optional, Union

YearType = Union[int, str]

class LeapYearVerifier:
    def is_leap(self, year: YearType) -> bool:
        if isinstance(year, str):
            if not year.isdigit():
                raise ValueError("Year string must contain only digits")
            year_value = int(year)
        else:
            year_value = year
        
        if year_value < 1:
            raise ValueError("Year must be a positive integer")
        
        if year_value % 400 == 0:
            return True
        if year_value % 100 == 0:
            return False
        if year_value % 4 == 0:
            return True
        return False

if __name__ == '__main__':
    verifier = LeapYearVerifier()
    test_years = [2000, 1900, 2024, 2023, "2024", "1900", "2000", "2023"]
    for t_year in test_years:
        result = verifier.is_leap(t_year)
        print(f"{t_year}: {result}")