from typing import Final

class LeapYearVerifier:
    DIVISIBLE_BY_4: Final[int] = 4
    DIVISIBLE_BY_100: Final[int] = 100
    DIVISIBLE_BY_400: Final[int] = 400
    MIN_YEAR: Final[int] = 1

    def __init__(self) -> None:
        self._verification_count: int = 0

    def _check_divisibility(self, year: int, divisor: int) -> bool:
        return year % divisor == 0

    def verify(self, year: int) -> bool:
        if year < self.MIN_YEAR:
            return False
        is_div_by_4 = self._check_divisibility(year, self.DIVISIBLE_BY_4)
        is_div_by_100 = self._check_divisibility(year, self.DIVISIBLE_BY_100)
        is_div_by_400 = self._check_divisibility(year, self.DIVISIBLE_BY_400)
        if not is_div_by_4:
            return False
        if is_div_by_100 and not is_div_by_400:
            return False
        return True

    def get_status(self, year: int) -> str:
        is_leap = self.verify(year)
        prefix = "is" if is_leap else "is not"
        return f"{year} {prefix} a leap year"

if __name__ == '__main__':
    verifier = LeapYearVerifier()
    test_years = [2000, 1900, 2024, 2023, 1600, 1700, 2100, 400]
    for year in test_years:
        print(verifier.get_status(year))
    print(verifier.verify(2000))
    print(verifier.verify(1900))