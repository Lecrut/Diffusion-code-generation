from datetime import date

HOLIDAYS = [
    date(2023, 12, 25),
    date(2024, 1, 1)
]

class DateChecker:
    def __init__(self):
        self.holidays = HOLIDAYS

    def is_weekend(self, given_date):
        return given_date.weekday() >= 5

    def is_holiday(self, given_date):
        return given_date in self.holidays

    def is_weekend_with_holidays(self, given_date):
        return self.is_weekend(given_date) or self.is_holiday(given_date)

if __name__ == '__main__':
    checker = DateChecker()
    sample_date1 = date(2023, 12, 26)
    sample_date2 = date(2024, 1, 1)
    print(checker.is_weekend_with_holidays(sample_date1))
    print(checker.is_weekend_with_holidays(sample_date2))