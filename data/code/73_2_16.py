from datetime import datetime, timedelta

class TimeCalculator:
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_DAY = 86400

    def __init__(self):
        self.last_result = None

    def calculate_difference(self, start_time: datetime, end_time: datetime) -> dict:
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise ValueError("Both inputs must be datetime objects")
        
        delta = end_time - start_time
        total_seconds = int(delta.total_seconds())
        
        is_negative = total_seconds < 0
        total_seconds = abs(total_seconds)
        
        days = total_seconds // self.SECONDS_PER_DAY
        remainder = total_seconds % self.SECONDS_PER_DAY
        
        hours = remainder // self.SECONDS_PER_HOUR
        remainder %= self.SECONDS_PER_HOUR
        
        minutes = remainder // self.SECONDS_PER_MINUTE
        seconds = remainder % self.SECONDS_PER_MINUTE
        
        result = {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": total_seconds,
            "is_negative": is_negative
        }
        
        self.last_result = result
        return result

    def get_last_result(self) -> dict:
        return self.last_result

if __name__ == '__main__':
    calculator = TimeCalculator()
    
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 5, 14, 30, 45)
    
    diff1 = calculator.calculate_difference(time1, time2)
    print(f"First Difference: {diff1}")
    
    time3 = datetime(2023, 12, 31, 23, 59, 59)
    time4 = datetime(2024, 1, 1, 0, 0, 1)
    
    diff2 = calculator.calculate_difference(time3, time4)
    print(f"Second Difference: {diff2}")
    
    last = calculator.get_last_result()
    print(f"Last Result Total Seconds: {last['total_seconds']}")