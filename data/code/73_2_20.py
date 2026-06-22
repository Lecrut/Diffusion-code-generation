from datetime import datetime, timedelta

class TimeCalculator:
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_DAY = 86400

    def __init__(self):
        self.last_result = None

    def calculate_difference(self, start_time: datetime, end_time: datetime) -> dict:
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise ValueError("Inputs must be datetime objects")
        
        delta = end_time - start_time
        total_seconds = int(delta.total_seconds())
        
        if total_seconds < 0:
            sign = -1
            total_seconds = abs(total_seconds)
        else:
            sign = 1
            
        days = total_seconds // self.SECONDS_PER_DAY
        remainder = total_seconds % self.SECONDS_PER_DAY
        
        hours = remainder // self.SECONDS_PER_HOUR
        remainder = remainder % self.SECONDS_PER_HOUR
        
        minutes = remainder // self.SECONDS_PER_MINUTE
        seconds = remainder % self.SECONDS_PER_MINUTE
        
        result = {
            "days": days * sign,
            "hours": hours * sign,
            "minutes": minutes * sign,
            "seconds": seconds * sign,
            "total_seconds": total_seconds * sign
        }
        
        self.last_result = result
        return result

    def get_last_result(self) -> dict:
        return self.last_result

if __name__ == '__main__':
    calculator = TimeCalculator()
    
    t1 = datetime(2023, 1, 1, 0, 0, 0)
    t2 = datetime(2023, 1, 2, 1, 1, 1)
    
    res1 = calculator.calculate_difference(t1, t2)
    print(res1)
    
    t3 = datetime(2023, 12, 31, 23, 59, 59)
    t4 = datetime(2024, 1, 1, 0, 0, 0)
    
    res2 = calculator.calculate_difference(t3, t4)
    print(res2)
    
    last = calculator.get_last_result()
    print(last)