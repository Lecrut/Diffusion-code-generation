class LeapYearChecker:
    def is_leap_year(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    checker = LeapYearChecker()
    print(checker.is_leap_year(2000))
    print(checker.is_leap_year(1900))
    print(checker.is_leap_year(2020))
    print(checker.is_leap_year(2021))