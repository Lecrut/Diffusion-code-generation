class LeapYearChecker:
    DIVISOR_FOUR = 4
    DIVISOR_HUNDRED = 100
    DIVISOR_FOUR_HUNDRED = 400

    @staticmethod
    def is_leap(year):
        if year % LeapYearChecker.DIVISOR_FOUR_HUNDRED == 0:
            return True
        if year % LeapYearChecker.DIVISOR_HUNDRED == 0:
            return False
        return year % LeapYearChecker.DIVISOR_FOUR == 0

if __name__ == '__main__':
    cases = [2000, 1900, 2024]
    for year in cases:
        print(LeapYearChecker.is_leap(year))