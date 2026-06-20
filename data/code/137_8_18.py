class LeapYearChecker:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    print(f"Is 2000 a leap year? {LeapYearChecker.is_leap_year(2000)}")
    print(f"Is 1900 a leap year? {LeapYearChecker.is_leap_year(1900)}")
    print(f"Is 2020 a leap year? {LeapYearChecker.is_leap_year(2020)}")
    print(f"Is 2023 a leap year? {LeapYearChecker.is_leap_year(2023)}")