import datetime

class TimeCalculator:
    def calculate_difference(self, start: datetime.datetime, end: datetime.datetime):
        if not isinstance(start, datetime.datetime) or not isinstance(end, datetime.datetime):
            raise ValueError("Inputs must be datetime objects")
        
        delta = end - start
        total_seconds = int(delta.total_seconds())
        
        if total_seconds < 0:
            total_seconds = -total_seconds
        
        days = total_seconds // 86400
        remaining = total_seconds % 86400
        
        hours = remaining // 3600
        remaining %= 3600
        
        minutes = remaining // 60
        seconds = remaining % 60
        
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

if __name__ == '__main__':
    calculator = TimeCalculator()
    start_time = datetime.datetime(2023, 6, 15, 8, 30, 0)
    end_time = datetime.datetime(2023, 6, 18, 11, 45, 30)
    
    result = calculator.calculate_difference(start_time, end_time)
    print(result)