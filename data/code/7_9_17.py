import datetime
from typing import Union

def calculate_time_difference(start: datetime.datetime, end: datetime.datetime, unit: str = 'days') -> Union[float, tuple]:
    if start > end:
        raise ValueError("Start time must be before end time")
    
    delta = end - start
    total_seconds = delta.total_seconds()
    
    if unit == 'seconds':
        return total_seconds
    elif unit == 'minutes':
        return total_seconds / 60
    elif unit == 'hours':
        return total_seconds / 3600
    elif unit == 'days':
        return total_seconds / 86400
    elif unit == 'mixed':
        days = int(total_seconds // 86400)
        remaining_seconds = total_seconds % 86400
        hours = int(remaining_seconds // 3600)
        remaining_seconds %= 3600
        minutes = int(remaining_seconds // 60)
        seconds = int(remaining_seconds % 60)
        return (days, hours, minutes, seconds)
    else:
        raise ValueError(f"Unsupported unit: {unit}. Choose from 'seconds', 'minutes', 'hours', 'days', or 'mixed'")

if __name__ == '__main__':
    start_time = datetime.datetime(2023, 1, 1, 8, 0, 0)
    end_time = datetime.datetime(2023, 1, 3, 14, 30, 45)
    
    days_diff = calculate_time_difference(start_time, end_time, 'days')
    hours_diff = calculate_time_difference(start_time, end_time, 'hours')
    mixed_diff = calculate_time_difference(start_time, end_time, 'mixed')
    
    print(days_diff)
    print(hours_diff)
    print(mixed_diff)