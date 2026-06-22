import datetime

def calculate_time_difference(start_dt: datetime.datetime, end_dt: datetime.datetime, unit: str = "seconds") -> float:
    if not isinstance(start_dt, datetime.datetime) or not isinstance(end_dt, datetime.datetime):
        raise TypeError("Both arguments must be datetime.datetime objects")
    
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    
    if unit == "seconds":
        return total_seconds
    if unit == "minutes":
        return total_seconds / 60
    if unit == "hours":
        return total_seconds / 3600
    if unit == "days":
        return total_seconds / 86400
    
    raise ValueError(f"Unsupported unit: {unit}")

def format_time_difference(start_dt: datetime.datetime, end_dt: datetime.datetime) -> dict:
    delta = end_dt - start_dt
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

if __name__ == "__main__":
    start = datetime.datetime(2023, 1, 1, 10, 30, 0)
    end = datetime.datetime(2023, 1, 5, 14, 45, 30)
    
    diff_seconds = calculate_time_difference(start, end, "seconds")
    print(diff_seconds)
    
    formatted = format_time_difference(start, end)
    print(formatted)