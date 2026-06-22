class YearDifferenceCalculator:
    YEAR_OFFSET = 0
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def _parse_year(date_string: str) -> int:
        parts = date_string.split("-")
        return int(parts[0])

    def calculate(self, date1: str, date2: str) -> int:
        year1 = self._parse_year(date1)
        year2 = self._parse_year(date2)
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    result = calculator.calculate("2010-05-20", "2025-08-15")
    print(result)