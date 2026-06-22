class LeapYearChecker:
    FOUR = 4
    HUNDRED = 100
    FOUR_HUNDRED = 400

    @staticmethod
    def is_leap(year):
        if year % LeapYearChecker.FOUR != 0:
            return False
        if year % LeapYearChecker.HUNDRED != 0:
            return True
        return year % LeapYearChecker.FOUR_HUNDRED == 0

if __name__ == '__main__':
    print(LeapYearChecker.is_leap(2000))
    print(LeapYearChecker.is_leap(1900))
    print(LeapYearChecker.is_leap(2024))
    print(LeapYearChecker.is_leap(2023))
    print(LeapYearChecker.is_leap(2400))
    print(LeapYearChecker.is_leap(2100))