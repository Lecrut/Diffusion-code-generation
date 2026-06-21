from datetime import datetime

class IsoFormatter:
    def __init__(self, dt: datetime):
        self.dt = dt

    def to_iso_string(self) -> str:
        y = self.dt.year
        m = self.dt.month
        d = self.dt.day
        h = self.dt.hour
        mi = self.dt.minute
        s = self.dt.second
        return f"{y}-{m:02}-{d:02} {h:02}:{mi:02}:{s:02}"

    def get_year(self) -> int:
        return self.dt.year

    def get_month(self) -> int:
        return self.dt.month

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatter = IsoFormatter(sample_dt)
    print(formatter.to_iso_string())
    print(formatter.get_year())
    print(formatter.get_month())