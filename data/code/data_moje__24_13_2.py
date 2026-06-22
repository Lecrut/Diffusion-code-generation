class LeapYearChecker:
    def __init__(self) -> None:
        self._test_cases: list[int] = [2000, 1900, 2024, 2023, 2400, 1600, 1700]

    def _is_divisible_by(self, number: int, divisor: int) -> bool:
        return number % divisor == 0

    def check_leap_status(self, year: int) -> bool:
        divisible_by_4 = self._is_divisible_by(year, 4)
        divisible_by_100 = self._is_divisible_by(year, 100)
        divisible_by_400 = self._is_divisible_by(year, 400)
        if not divisible_by_4:
            return False
        if divisible_by_100:
            if divisible_by_400:
                return True
            return False
        return True

    def run_internal_tests(self) -> dict[int, bool]:
        results: dict[int, bool] = {}
        for test_year in self._test_cases:
            is_leap = self.check_leap_status(test_year)
            results[test_year] = is_leap
        return results

if __name__ == '__main__':
    checker = LeapYearChecker()
    test_results = checker.run_internal_tests()
    for year, status in test_results.items():
        print(f"{year}: {status}")