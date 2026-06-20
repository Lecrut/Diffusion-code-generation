import calendar

class DateChecker:
    def __init__(self):
        self.dates_to_check = [
            (2023, 10, 23),
            (2023, 10, 24),
            (2023, 10, 28),
            (2023, 10, 29)
        ]

    def is_weekday(self, year, month, day):
        return calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    checker = DateChecker()
    for date in checker.dates_to_check:
        print(f"Is {date[0]}/{date[1]}/{date[2]} a weekday? {checker.is_weekday(*date)}")