from typing import List, Tuple

class LeapYearValidator:
    def __init__(self) -> None:
        self._cache: dict[int, bool] = {}

    def is_leap_year(self, year: int) -> bool:
        if year in self._cache:
            return self._cache[year]
        result = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        self._cache[year] = result
        return result

    def get_leap_year_status(self, year: int) -> str:
        if self.is_leap_year(year):
            return f"{year} is a leap year"
        return f"{year} is not a leap year"

    def batch_check(self, years: List[int]) -> List[Tuple[int, bool]]:
        results: List[Tuple[int, bool]] = []
        for year in years:
            results.append((year, self.is_leap_year(year)))
        return results

if __name__ == "__main__":
    validator = LeapYearValidator()
    sample_years = [2000, 1900, 2024, 2023, 2100, 2400]
    
    for year in sample_years:
        status = validator.get_leap_year_status(year)
        print(status)
    
    batch_results = validator.batch_check([2004, 2005, 2006, 2007, 2008])
    for year, is_leap in batch_results:
        print(f"{year}: {is_leap}")