import calendar

class DateChecker:
    WEEKDAY_THRESHOLD = 5

    @staticmethod
    def is_weekday(year, month, day):
        return calendar.weekday(year, month, day) < DateChecker.WEEKDAY_THRESHOLD

if __name__ == '__main__':
    checker = DateChecker()
    print(f"Is 2023/10/23 a weekday? {checker.is_weekday(2023, 10, 23)}")
    print(f"Is 2023/10/24 a weekday? {checker.is_weekday(2023, 10, 24)}")
    print(f"Is 2023/10/28 a weekday? {checker.is_weekday(2023, 10, 28)}")
    print(f"Is 2023/10/29 a weekday? {checker.is_weekday(2023, 10, 29)}")