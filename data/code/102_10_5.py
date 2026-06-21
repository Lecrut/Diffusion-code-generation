import calendar
from datetime import datetime

class DateAnalyzer:
    def __init__(self, dt: datetime):
        if not isinstance(dt, datetime):
            raise ValueError("dt must be a datetime instance")
        self.dt = dt

    def is_weekday(self) -> bool:
        day_code = calendar.weekday(self.dt.year, self.dt.month, self.dt.day)
        return day_code < 5

    def day_name(self) -> str:
        return calendar.day_name[calendar.weekday(self.dt.year, self.dt.month, self.dt.day)]

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 25)
    analyzer = DateAnalyzer(sample_dt)
    print(analyzer.is_weekday())
    print(analyzer.day_name())