from datetime import datetime, timedelta

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

class TimeCalculator:
    def calculate_difference(self, start_time, end_time):
        if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
            raise ValueError("Both inputs must be datetime objects")
        
        delta = end_time - start_time
        total_seconds = int(delta.total_seconds())
        
        if total_seconds < 0:
            sign = -1
            total_seconds = -total_seconds
        else:
            sign = 1
            
        days = total_seconds // SECONDS_PER_DAY
        remainder = total_seconds % SECONDS_PER_DAY
        
        hours = remainder // SECONDS_PER_HOUR
        remainder %= SECONDS_PER_HOUR
        
        minutes = remainder // SECONDS_PER_MINUTE
        seconds = remainder % SECONDS_PER_MINUTE
        
        return sign * days, sign * hours, sign * minutes, sign * seconds

if __name__ == '__main__':
    calculator = TimeCalculator()
    t1 = datetime(2024, 1, 15, 10, 30, 45)
    t2 = datetime(2024, 1, 20, 14, 45, 15)
    days, hours, minutes, seconds = calculator.calculate_difference(t1, t2)
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")