import datetime

class LeapYearValidator:
    def is_leap_year(self, year: int) -> bool:
        if not isinstance(year, int):
            return False
        if year < 1:
            return False
        return datetime.date(year, 2, 29).day == 29

if __name__ == '__main__':
    validator = LeapYearValidator()
    test_years = [2000, 1900, 2024, 2023, 400, 500]
    results = [validator.is_leap_year(y) for y in test_years]
    for year, is_leap in zip(test_years, results):
        print(is_leap)