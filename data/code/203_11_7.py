from datetime import datetime, timedelta

class DateTimeComparator:
    def __init__(self, dt1, dt2):
        self.dt1 = dt1
        self.dt2 = dt2
    
    def time_difference_seconds(self):
        if not isinstance(self.dt1, datetime) or not isinstance(self.dt2, datetime):
            raise ValueError("Both inputs must be instances of datetime")
        
        delta = abs(self.dt1 - self.dt2)
        return int(delta.total_seconds())

if __name__ == '__main__':
    dt1 = datetime(2023, 4, 1, 12, 0, 0, tzinfo=timezone.utc)
    dt2 = datetime(2023, 4, 1, 14, 30, 0, tzinfo=timezone.utc)
    
    comparator = DateTimeComparator(dt1, dt2)
    difference_seconds = comparator.time_difference_seconds()
    print(difference_seconds)