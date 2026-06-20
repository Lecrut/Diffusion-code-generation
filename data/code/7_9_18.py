from datetime import datetime
from dataclasses import dataclass

@dataclass
class TimeBreakdown:
    days: int
    hours: int
    minutes: int
    seconds: int

    def __str__(self):
        return f"{self.days}d {self.hours}h {self.minutes}m {self.seconds}s"

def get_time_breakdown(dt_start: datetime, dt_end: datetime) -> TimeBreakdown:
    delta = dt_end - dt_start
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        total_seconds = -total_seconds
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return TimeBreakdown(days, hours, minutes, seconds)

def convert_to_unit(dt_start: datetime, dt_end: datetime, unit: str) -> float:
    delta = dt_end - dt_start
    total_seconds = abs(delta.total_seconds())
    if unit == "seconds":
        return total_seconds
    if unit == "minutes":
        return total_seconds / 60
    if unit == "hours":
        return total_seconds / 3600
    if unit == "days":
        return total_seconds / 86400
    if unit == "weeks":
        return total_seconds / 604800
    return total_seconds

if __name__ == "__main__":
    start_time = datetime(2023, 1, 1, 10, 0, 0)
    end_time = datetime(2023, 1, 5, 14, 30, 15)
    
    breakdown = get_time_breakdown(start_time, end_time)
    print(breakdown)
    
    total_hours = convert_to_unit(start_time, end_time, "hours")
    print(total_hours)