import datetime

def calculate_time_difference(start: datetime.datetime, end: datetime.datetime) -> dict:
    if not isinstance(start, datetime.datetime) or not isinstance(end, datetime.datetime):
        raise ValueError("Inputs must be datetime objects")
    
    delta = end - start
    total_seconds = abs(int(delta.total_seconds()))
    
    hours = total_seconds // 3600
    remainder_after_hours = total_seconds % 3600
    minutes = remainder_after_hours // 60
    seconds = remainder_after_hours % 60
    
    if delta.total_seconds() < 0:
        hours = -hours
    
    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    dt1 = datetime.datetime(2023, 1, 1, 10, 30, 45)
    dt2 = datetime.datetime(2023, 1, 1, 14, 15, 20)
    result = calculate_time_difference(dt1, dt2)
    print(result)