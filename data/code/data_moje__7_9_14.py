from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> dict:
    delta = end - start
    total_seconds = int(delta.total_seconds())
    
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 10, 30, 0)
    end_time = datetime(2023, 10, 5, 14, 45, 30)
    
    result = calculate_time_difference(start_time, end_time)
    print(result)