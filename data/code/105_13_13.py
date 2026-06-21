from datetime import date, timedelta

class WeekendFinder:
    def __init__(self, start_date=None):
        self.start_date = start_date if start_date is not None else date.today()
        self.weekend_days = {5, 6}

    def get_next_weekend_date(self):
        current = self.start_date
        while current.weekday() not in self.weekend_days:
            current += timedelta(days=1)
        return current

    def get_days_until_weekend(self):
        current = self.start_date
        days = 0
        while current.weekday() not in self.weekend_days:
            current += timedelta(days=1)
            days += 1
        return days

if __name__ == '__main__':
    finder = WeekendFinder()
    next_weekend = finder.get_next_weekend_date()
    days_count = finder.get_days_until_weekend()
    print(next_weekend)
    print(days_count)