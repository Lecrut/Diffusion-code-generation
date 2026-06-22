from datetime import datetime
from dataclasses import dataclass
from typing import Tuple

@dataclass
class TimeDelta:
    hours: int
    minutes: int
    seconds: int

    def __post_init__(self):
        if self.seconds < 0:
            self.seconds = -self.seconds
            self.minutes = -self.minutes
            self.hours = -self.hours

def get_time_components(start: datetime, end: datetime) -> TimeDelta:
    total_seconds = int((end - start).total_seconds())
    if total_seconds == 0:
        return TimeDelta(0, 0, 0)
    
    sign = 1 if total_seconds > 0 else -1
    abs_seconds = abs(total_seconds)
    
    hours = abs_seconds // 3600
    remainder = abs_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    
    return TimeDelta(sign * hours, sign * minutes, sign * seconds)

if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 10, 0, 0)
    end_time = datetime(2023, 10, 1, 14, 30, 45)
    result = get_time_components(start_time, end_time)
    print(f"{result.hours} hours, {result.minutes} minutes, {result.seconds} seconds")