from datetime import datetime, timedelta

def calculate_time_left_in_month(start_date: datetime, end_date: datetime) -> dict:
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")
    
    delta = end_date - start_date
    total_seconds = int(delta.total_seconds())
    
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    
    hours = remainder // 3600
    remainder %= 3600
    
    minutes = remainder // 60
    seconds = remainder % 60
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "total_seconds": total_seconds
    }

if __name__ == '__main__':
    start = datetime(2023, 10, 1, 10, 30, 0)
    end = datetime(2023, 10, 31, 23, 59, 59)
    result = calculate_time_left_in_month(start, end)
    print(result)