from datetime import date, timedelta

class DateRangeChecker:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date

    def is_weekend_in_range(self) -> bool:
        current_date = self.start_date
        while current_date <= self.end_date:
            if current_date.weekday() >= 5:
                return True
            current_date += timedelta(days=1)
        return False

if __name__ == '__main__':
    checker = DateRangeChecker(date(2023, 4, 1), date(2023, 4, 7))
    print(checker.is_weekend_in_range())