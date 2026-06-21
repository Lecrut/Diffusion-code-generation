class LeapYearValidator:
    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

if __name__ == '__main__':
    validator = LeapYearValidator()
    test_years = [2000, 1900, 2024, 2023, 400, 100]
    results = [validator.is_leap_year(y) for y in test_years]
    print(results)