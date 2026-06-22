from datetime import datetime

TIME_SECONDS_IN_MINUTE = 60
TIME_SECONDS_IN_HOUR = 3600
TIME_SECONDS_IN_DAY = 86400
TIME_SECONDS_IN_WEEK = 604800

class TimeDiffEngine:
    def __init__(self, first: datetime, second: datetime):
        self.start = first
        self.stop = second

    def get_seconds(self) -> float:
        diff = self.stop - self.start
        return abs(diff.total_seconds())

    def to_unit(self, unit: str) -> float:
        total_secs = self.get_seconds()
        if unit == 'seconds':
            return total_secs
        if unit == 'minutes':
            return total_secs / TIME_SECONDS_IN_MINUTE
        if unit == 'hours':
            return total_secs / TIME_SECONDS_IN_HOUR
        if unit == 'days':
            return total_secs / TIME_SECONDS_IN_DAY
        if unit == 'weeks':
            return total_secs / TIME_SECONDS_IN_WEEK
        return total_secs

    def to_composite(self) -> str:
        total_secs = self.get_seconds()
        days = int(total_secs // TIME_SECONDS_IN_DAY)
        remaining_after_days = total_secs % TIME_SECONDS_IN_DAY
        
        hours = int(remaining_after_days // TIME_SECONDS_IN_HOUR)
        remaining_after_hours = remaining_after_days % TIME_SECONDS_IN_HOUR
        
        minutes = int(remaining_after_hours // TIME_SECONDS_IN_MINUTE)
        
        return f"{days}d {hours}h {minutes}m"

if __name__ == '__main__':
    start_dt = datetime(2023, 5, 10, 8, 30, 0)
    end_dt = datetime(2023, 6, 15, 14, 45, 30)
    
    engine = TimeDiffEngine(start_dt, end_dt)
    
    hours_result = engine.to_unit('hours')
    print(hours_result)
    
    composite_result = engine.to_composite()
    print(composite_result)