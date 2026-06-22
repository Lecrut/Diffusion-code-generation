from datetime import date

class DateChecker:
    def is_weekend(self, date):
        if not isinstance(date, date):
            raise ValueError("Input must be a date object")
        weekday = date.weekday()
        return weekday >= 5

if __name__ == '__main__':
    checker = DateChecker()
    dates = [date(2023, 10, 6), date(2023, 10, 7), date(2023, 10, 8)]
    for d in dates:
        print(f"Is {d} a weekend? {checker.is_weekend(d)}")