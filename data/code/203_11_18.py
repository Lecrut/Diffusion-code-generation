from datetime import datetime, timedelta

class DateTimeComparator:
    def __init__(self, dt1: datetime, dt2: datetime):
        self.dt1 = dt1
        self.dt2 = dt2
    
    def get_difference_seconds(self) -> int:
        delta = abs(self.dt1 - self.dt2)
        return delta.total_seconds()

if __name__ == '__main__':
    dt1 = datetime(2023, 10, 1, 12, 0, 0, tzinfo=None)
    dt2 = datetime(2023, 10, 1, 12, 0, 30, tzinfo=None)
    
    comparator = DateTimeComparator(dt1, dt2)
    difference_seconds = comparator.get_difference_seconds()
    
    print(f"Difference in seconds: {difference_seconds}")