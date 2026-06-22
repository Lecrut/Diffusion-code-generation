class LeapYearChecker:
    def is_leap_year(self, year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

if __name__ == '__main__':
    checker = LeapYearChecker()
    print(checker.is_leap_year(2400))
    print(checker.is_leap_year(2100))
    print(checker.is_leap_year(2024))
    print(checker.is_leap_year(2023))