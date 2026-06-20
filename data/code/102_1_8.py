import calendar

class DateChecker:
    WEEKDAY_THRESHOLD = 5

    @staticmethod
    def is_weekday(year, month, day):
        return calendar.weekday(year, month, day) < DateChecker.WEEKDAY_THRESHOLD

if __name__ == '__main__':
    checker = DateChecker()
    dates_to_check = [
        (2023, 10, 23),
        (2023, 10, 24),
        (2023, 10, 28),
        (2023, 10, 29)
    ]
    for date in dates_to_check:
        print(f"Is {date[0]}/{date[1]}/{date[2]} a weekday? {checker.is_weekday(*date)}")