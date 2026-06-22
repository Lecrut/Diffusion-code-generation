from datetime import datetime, timedelta

class DateTimeComparator:
    def __init__(self, dt1: datetime, dt2: datetime):
        if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
            raise ValueError("Both inputs must be datetime instances")
        self.dt1 = dt1
        self.dt2 = dt2

    def compare(self) -> str:
        if self.dt1 < self.dt2:
            return "First is earlier"
        if self.dt1 > self.dt2:
            return "Second is earlier"
        return "They are equal"

if __name__ == '__main__':
    base_time = datetime(2024, 5, 10, 10, 30, 0)
    later_time = base_time + timedelta(hours=2)
    earlier_time = base_time - timedelta(hours=2)
    
    comp = DateTimeComparator(earlier_time, later_time)
    result = comp.compare()
    print(result)