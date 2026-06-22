import calendar
from datetime import datetime

def time_remaining_in_month(year: int, month: int) -> dict:
    if not isinstance(year, int) or not isinstance(month, int):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be positive")

    target_start = datetime(year, month, 1)
    target_end = datetime(year, month, calendar.monthrange(year, month)[1], 23, 59, 59)
    now = datetime.now()

    if now >= target_end:
        return {"hours": 0, "minutes": 0, "seconds": 0}
    
    if now < target_start:
        remaining_seconds = (target_end - target_start).total_seconds()
    else:
        remaining_seconds = (target_end - now).total_seconds()

    total_seconds = int(remaining_seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    result = time_remaining_in_month(2024, 12)
    print(result)