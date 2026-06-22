from datetime import datetime

class Iso8601Formatter:
    def __init__(self, dt: datetime):
        if not isinstance(dt, datetime):
            raise ValueError("Input must be a datetime object")
        self.dt = dt

    def format_iso8601(self) -> str:
        year = self.dt.year
        month = self.dt.month
        day = self.dt.day
        hour = self.dt.hour
        minute = self.dt.minute
        second = self.dt.second
        if not (1 <= month <= 12):
            raise ValueError("Invalid month")
        if not (1 <= day <= 31):
            raise ValueError("Invalid day")
        if not (0 <= hour <= 23):
            raise ValueError("Invalid hour")
        if not (0 <= minute <= 59):
            raise ValueError("Invalid minute")
        if not (0 <= second <= 59):
            raise ValueError("Invalid second")
        return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

    def get_date_part(self) -> str:
        return f"{self.dt.year}-{self.dt.month:02d}-{self.dt.day:02d}"

    def get_time_part(self) -> str:
        return f"{self.dt.hour:02d}:{self.dt.minute:02d}:{self.dt.second:02d}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatter = Iso8601Formatter(sample_dt)
    print(formatter.format_iso8601())
    print(formatter.get_date_part())
    print(formatter.get_time_part())