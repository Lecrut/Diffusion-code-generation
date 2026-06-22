from datetime import date

class DateChecker:
    def is_weekend(self, date):
        return date.weekday() >= 5

if __name__ == '__main__':
    checker = DateChecker()
    dates_to_check = [date(2023, 10, 6), date(2023, 10, 7), date(2023, 10, 8)]
    for dt in dates_to_check:
        print(f"Is {dt} a weekend? {checker.is_weekend(dt)}")