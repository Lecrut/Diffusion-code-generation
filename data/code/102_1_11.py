import calendar

class DateChecker:
    def __init__(self):
        self.holiday_dates = [(2023, 10, 28), (2023, 10, 29)]

    def is_weekday(self, year, month, day):
        return calendar.weekday(year, month, day) < 5

    def check_holidays(self):
        results = {}
        for date in self.holiday_dates:
            results[date] = self.is_weekday(*date)
        return results

if __name__ == '__main__':
    checker = DateChecker()
    print(checker.check_holidays())