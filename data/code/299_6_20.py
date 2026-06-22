from datetime import date

class DateChecker:
    HOLIDAYS = [date(2023, 12, 25), date(2024, 1, 1)]

    @staticmethod
    def is_weekend_with_holidays(given_date):
        return given_date.weekday() >= 5 or given_date in DateChecker.HOLIDAYS

if __name__ == '__main__':
    checker = DateChecker()
    sample_date = date(2023, 12, 26)
    print(checker.is_weekend_with_holidays(sample_date))