class ChronoLeapVerifier:
    RULE_DIVISOR_4: int = 4
    RULE_DIVISOR_100: int = 100
    RULE_DIVISOR_400: int = 400

    def __init__(self) -> None:
        self._history: dict[int, bool] = {}

    def _validate_positive(self, year: int) -> None:
        if year <= 0:
            raise ValueError("Year must be a positive integer")

    def _check_divisibility(self, value: int, divisor: int) -> bool:
        return value % divisor == 0

    def verify_single(self, year: int) -> bool:
        self._validate_positive(year)
        if year in self._history:
            return self._history[year]
        is_div_4 = self._check_divisibility(year, self.RULE_DIVISOR_4)
        is_div_100 = self._check_divisibility(year, self.RULE_DIVISOR_100)
        is_div_400 = self._check_divisibility(year, self.RULE_DIVISOR_400)
        result = False
        if is_div_4:
            if not is_div_100:
                result = True
            else:
                if is_div_400:
                    result = True
                else:
                    result = False
        self._history[year] = result
        return result

    def batch_verify(self, years: list[int]) -> dict[int, bool]:
        results: dict[int, bool] = {}
        for current_year in years:
            results[current_year] = self.verify_single(current_year)
        return results

    def count_leaps(self, start: int, end: int) -> int:
        self._validate_positive(start)
        self._validate_positive(end)
        if start > end:
            return 0
        counter: int = 0
        for y in range(start, end + 1):
            if self.verify_single(y):
                counter += 1
        return counter

    def get_status_report(self, year: int) -> str:
        status = "leap" if self.verify_single(year) else "non-leap"
        return f"Year {year} is a {status} year"

if __name__ == '__main__':
    verifier = ChronoLeapVerifier()
    sample_years: list[int] = [2000, 1900, 2024, 2023, 400, 100, 2400, 2001]
    batch_results: dict[int, bool] = verifier.batch_verify(sample_years)
    for year, is_leap in batch_results.items():
        print(f"{year}: {is_leap}")
    range_start: int = 2020
    range_end: int = 2032
    count = verifier.count_leaps(range_start, range_end)
    print(f"Leap years between {range_start} and {range_end}: {count}")
    test_report_year: int = 1996
    print(verifier.get_status_report(test_report_year))