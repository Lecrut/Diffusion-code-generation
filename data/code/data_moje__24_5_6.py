class LeapYearChecker:
    @staticmethod
    def is_divisible_by_four(year: int) -> bool:
        return year % 4 == 0

    @staticmethod
    def is_divisible_by_hundred(year: int) -> bool:
        return year % 100 == 0

    @staticmethod
    def is_divisible_by_four_hundred(year: int) -> bool:
        return year % 400 == 0

    @staticmethod
    def check_leap(year: int) -> bool:
        if not LeapYearChecker.is_divisible_by_four(year):
            return False
        if not LeapYearChecker.is_divisible_by_hundred(year):
            return True
        return LeapYearChecker.is_divisible_by_four_hundred(year)

if __name__ == '__main__':
    test_cases = [1600, 1700, 2400, 2300, 2025]
    for year in test_cases:
        print(LeapYearChecker.check_leap(year))