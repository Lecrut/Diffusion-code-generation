from datetime import datetime, timedelta

MONTH_CONFIG = {
    1: (31, timedelta(days=31)),
    2: (28, timedelta(days=28)),
    3: (31, timedelta(days=31)),
    4: (30, timedelta(days=30)),
    5: (31, timedelta(days=31)),
    6: (30, timedelta(days=30)),
    7: (31, timedelta(days=31)),
    8: (31, timedelta(days=31)),
    9: (30, timedelta(days=30)),
    10: (31, timedelta(days=31)),
    11: (30, timedelta(days=30)),
    12: (31, timedelta(days=31)),
}

def compute_remaining_month_time(year: int, month: int, day: int, hour: int, minute: int, second: int) -> timedelta:
    if month not in MONTH_CONFIG:
        raise ValueError(f"Invalid month: {month}")
    
    days_in_month, total_month_duration = MONTH_CONFIG[month]
    
    start_dt = datetime(year, month, 1)
    end_dt = datetime(year, month, days_in_month, 23, 59, 59)
    current_dt = datetime(year, month, day, hour, minute, second)
    
    if current_dt < start_dt:
        return total_month_duration
    elif current_dt > end_dt:
        return timedelta(0)
    else:
        return end_dt - current_dt

if __name__ == '__main__':
    result = compute_remaining_month_time(2023, 10, 15, 12, 0, 0)
    print(result)