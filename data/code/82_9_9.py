class YearDifferenceCalculator:
    MIN_YEAR = 1800
    MAX_YEAR = 2500

    @staticmethod
    def validate_year(year):
        if not isinstance(year, int) or year < YearDifferenceCalculator.MIN_YEAR or year > YearDifferenceCalculator.MAX_YEAR:
            raise ValueError(f"Year must be an integer between {YearDifferenceCalculator.MIN_YEAR} and {YearDifferenceCalculator.MAX_YEAR}")

    @classmethod
    def calculate_difference(cls, year1, year2):
        cls.validate_year(year1)
        cls.validate_year(year2)
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    difference = calculator.calculate_difference(2024, 1999)
    print(difference)