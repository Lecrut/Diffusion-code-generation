from datetime import datetime, timedelta

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

class TimeCalculator:
    def calculate_difference(self, start_time: datetime, end_time: datetime) -> dict:
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise ValueError("Inputs must be datetime objects")
        
        delta = end_time - start_time
        total_seconds = abs(int(delta.total_seconds()))
        
        days = total_seconds // SECONDS_PER_DAY
        remainder = total_seconds % SECONDS_PER_DAY
        
        hours = remainder // SECONDS_PER_HOUR
        remainder %= SECONDS_PER_HOUR
        
        minutes = remainder // SECONDS_PER_MINUTE
        seconds = remainder % SECONDS_PER_MINUTE
        
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

if __name__ == '__main__':
    calculator = TimeCalculator()
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 5, 14, 30, 45)
    result = calculator.calculate_difference(t1, t2)
    print(result)