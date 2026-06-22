import datetime

def calculate_time_difference(start_datetime: datetime.datetime, end_datetime: datetime.datetime) -> dict:
    if start_datetime > end_datetime:
        raise ValueError("Start datetime must be before end datetime")
    
    delta = end_datetime - start_datetime
    total_seconds = int(delta.total_seconds())
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

def format_time_difference(result: dict) -> str:
    days = result["days"]
    hours = result["hours"]
    minutes = result["minutes"]
    seconds = result["seconds"]
    
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    return " ".join(parts)

if __name__ == '__main__':
    start = datetime.datetime(2023, 1, 1, 10, 30, 0)
    end = datetime.datetime(2023, 1, 5, 14, 45, 20)
    
    result = calculate_time_difference(start, end)
    formatted = format_time_difference(result)
    
    print(formatted)