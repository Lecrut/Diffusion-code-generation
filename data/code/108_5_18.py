from datetime import datetime

class DateParser:
    def __init__(self, dt: datetime):
        self.dt = dt

    def get_day(self) -> int:
        return self.dt.day

    def get_full_date_string(self) -> str:
        return f"{self.dt.year}-{self.dt.month:02d}-{self.dt.day:02d}"

if __name__ == '__main__':
    parser = DateParser(datetime(2024, 7, 25))
    day = parser.get_day()
    print(day)
    print(parser.get_full_date_string())