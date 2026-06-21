class LeapYearChecker:
    def __init__(self) -> None:
        self.validation_cache: dict[int, bool] = {}

    def is_leap_year(self, year: int) -> bool:
        if year in self.validation_cache:
            return self.validation_cache[year]

        if year % 400 == 0:
            result = True
        elif year % 100 == 0:
            result = False
        elif year % 4 == 0:
            result = True
        else:
            result = False

        self.validation_cache[year] = result
        return result

if __name__ == '__main__':
    checker = LeapYearChecker()
    test_years = [1600, 1700, 1800, 1900, 2000, 2001, 2004, 2023, 2024]
    for year in test_years:
        print(checker.is_leap_year(year))