class LeapYearChecker:
    DIVISOR_FOUR = 4
    DIVISOR_HUNDRED = 100
    DIVISOR_FOUR_HUNDRED = 400

    @staticmethod
    def check(year):
        if LeapYearChecker._is_multiple(year, LeapYearChecker.DIVISOR_FOUR_HUNDRED):
            return True
        if LeapYearChecker._is_multiple(year, LeapYearChecker.DIVISOR_HUNDRED):
            return False
        return LeapYearChecker._is_multiple(year, LeapYearChecker.DIVISOR_FOUR)

    @staticmethod
    def _is_multiple(number, divisor):
        return number % divisor == 0

if __name__ == '__main__':
    test_values = [2000, 1900, 2024]
    for val in test_values:
        print(LeapYearChecker.check(val))