from datetime import datetime
from typing import Optional

class IsoFormatter:
    def __init__(self, dt: Optional[datetime] = None):
        self.dt = dt if dt is not None else datetime.now()

    def format(self) -> str:
        return f"{self.dt.year:04d}-{self.dt.month:02d}-{self.dt.day:02d} {self.dt.hour:02d}:{self.dt.minute:02d}:{self.dt.second:02d}"

    def get_year(self) -> int:
        return self.dt.year

if __name__ == '__main__':
    sample_dt = datetime(2024, 1, 15, 9, 30, 45)
    formatter = IsoFormatter(sample_dt)
    print(formatter.format())
    print(formatter.get_year())