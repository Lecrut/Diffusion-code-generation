from typing import Optional, List, Tuple

class LeapYearChecker:
    def __init__(self) -> None:
        self._history: List[Tuple[int, bool]] = []

    def is_leap_year(self, year: int) -> bool:
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < 1:
            raise ValueError("Year must be positive")
        
        is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
        self._history.append((year, is_leap))
        return is_leap

    def get_history(self) -> List[Tuple[int, bool]]:
        return list(self._history)

if __name__ == '__main__':
    checker = LeapYearChecker()
    test_years = [2000, 1900, 2024, 2023, 2100, 2400]
    
    for year in test_years:
        result = checker.is_leap_year(year)
        print(f"{year}: {result}")
    
    print(checker.get_history())