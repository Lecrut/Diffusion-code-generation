from datetime import date, timedelta

class WeekendFinder:
    def __init__(self, start_date=None):
        self.current_date = start_date if start_date is not None else date.today()
        self.weekend_days = {5, 6}

    def get_next_weekend_date(self):
        target = self.current_date
        while target.weekday() not in self.weekend_days:
            target += timedelta(days=1)
        return target

    def get_next_saturday(self):
        target = self.current_date
        while target.weekday() != 5:
            target += timedelta(days=1)
        return target

    def get_next_sunday(self):
        target = self.current_date
        while target.weekday() != 6:
            target += timedelta(days=1)
        return target

if __name__ == '__main__':
    finder = WeekendFinder()
    print(finder.get_next_weekend_date())
    print(finder.get_next_saturday())
    print(finder.get_next_sunday())