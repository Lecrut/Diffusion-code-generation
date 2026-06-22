import datetime

class TimeDifferenceCalculator:
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    @staticmethod
    def calculate(start: datetime.datetime, end: datetime.datetime) -> dict:
        delta = end - start
        total_seconds = int(delta.total_seconds())
        
        if total_seconds >= 0:
            sign = 1
            abs_seconds = total_seconds
        else:
            sign = -1
            abs_seconds = -total_seconds
            
        hours = abs_seconds // TimeDifferenceCalculator.SECONDS_PER_HOUR
        remainder_after_hours = abs_seconds % TimeDifferenceCalculator.SECONDS_PER_HOUR
        
        minutes = remainder_after_hours // TimeDifferenceCalculator.SECONDS_PER_MINUTE
        seconds = remainder_after_hours % TimeDifferenceCalculator.SECONDS_PER_MINUTE
        
        return {
            "hours": sign * hours,
            "minutes": sign * minutes,
            "seconds": sign * seconds
        }

if __name__ == '__main__':
    start_time = datetime.datetime(2023, 10, 1, 10, 30, 0)
    end_time = datetime.datetime(2023, 10, 1, 14, 45, 15)
    
    result = TimeDifferenceCalculator.calculate(start_time, end_time)
    
    print(result)