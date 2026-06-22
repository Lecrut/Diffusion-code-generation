from datetime import datetime, timedelta

class TimeCalculator:
    SECONDS_PER_DAY = 86400
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def compute_delta(self, start: datetime, end: datetime) -> dict:
        if not isinstance(start, datetime) or not isinstance(end, datetime):
            raise ValueError("Both arguments must be datetime instances")
        if start > end:
            raise ValueError("Start time must be earlier than or equal to end time")
        
        delta = end - start
        total_seconds = int(delta.total_seconds())
        
        days = total_seconds // self.SECONDS_PER_DAY
        remaining = total_seconds % self.SECONDS_PER_DAY
        
        hours = remaining // self.SECONDS_PER_HOUR
        remaining %= self.SECONDS_PER_HOUR
        
        minutes = remaining // self.SECONDS_PER_MINUTE
        seconds = remaining % self.SECONDS_PER_MINUTE
        
        return {
            "total_seconds": total_seconds,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

if __name__ == '__main__':
    calculator = TimeCalculator()
    t1 = datetime(2023, 1, 1, 0, 0, 0)
    t2 = datetime(2023, 1, 10, 12, 30, 45)
    result = calculator.compute_delta(t1, t2)
    print(result)