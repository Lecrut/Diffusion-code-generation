class LeapYearChecker:
    DIVISIBLE_BY_4_MASK = 3
    DIVISIBLE_BY_100_DIVISOR = 100
    DIVISIBLE_BY_400_DIVISOR = 400
    DIVISIBLE_BY_400_MASK = 31

    def is_leap(self, year: int) -> bool:
        if not self._is_divisible_by_four(year):
            return False
        if self._is_not_divisible_by_hundred(year):
            return True
        return self._is_divisible_by_four_hundred(year)

    def _is_divisible_by_four(self, year: int) -> bool:
        return (year & self.DIVISIBLE_BY_4_MASK) == 0

    def _is_not_divisible_by_hundred(self, year: int) -> bool:
        return year % self.DIVISIBLE_BY_100_DIVISOR != 0

    def _is_divisible_by_four_hundred(self, year: int) -> bool:
        return (year & self.DIVISIBLE_BY_400_MASK) == 0

    def run_assertions(self) -> list[bool]:
        test_cases = [
            (2000, True),
            (1900, False),
            (2024, True),
            (2023, False),
            (1600, True),
            (1700, False),
            (1800, False),
            (2400, True),
            (2100, False),
            (1000, False),
            (1200, True),
            (1300, False),
            (1400, False),
            (1500, False),
            (1100, False),
            (2300, False),
            (2500, False),
            (2600, False),
            (2700, False),
            (2800, True),
        ]
        results = []
        for year, expected in test_cases:
            result = self.is_leap(year)
            assert result is expected, f"Failed for year {year}"
            results.append(result)
        return results

if __name__ == '__main__':
    checker = LeapYearChecker()
    output = checker.run_assertions()
    print(output)
    print(checker.is_leap(2024))
    print(checker.is_leap(2100))