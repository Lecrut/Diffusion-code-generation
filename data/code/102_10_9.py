import calendar
from datetime import datetime

class WeekdayChecker:
    def __init__(self, dt: datetime):
        self.dt = dt

    def is_weekday(self) -> bool:
        day_code = calendar.weekday(self.dt.year, self.dt.month, self.dt.day)
        return day_code < 5

    def get_weekday_name(self) -> str:
        day_code = calendar.weekday(self.dt.year, self.dt.month, self.dt.day)
        return calendar.day_name[day_code]

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 25)
    checker = WeekdayChecker(sample_dt)
    print(checker.is_weekday())
    print(checker.get_weekday_name())