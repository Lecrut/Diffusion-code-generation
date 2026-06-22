class YearDifferenceCalculator:
    DATE_FORMAT = "%Y-%m-%d"
    YEAR_INDEX_END = 4

    @staticmethod
    def _parse_year(date_string: str) -> int:
        return int(date_string[:YearDifferenceCalculator.YEAR_INDEX_END])

    @classmethod
    def compute(cls, date1_str: str, date2_str: str) -> int:
        year1 = cls._parse_year(date1_str)
        year2 = cls._parse_year(date2_str)
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    result = calculator.compute("2020-01-01", "2023-12-31")
    print(result)