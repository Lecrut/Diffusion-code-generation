from datetime import datetime, timedelta

BASE_SECOND = 1
BASE_MINUTE = 60
BASE_HOUR = 3600
BASE_DAY = 86400

def calculate_time_difference(start: datetime, end: datetime, unit: str) -> float:
    delta = end - start
    total_seconds = abs(delta.total_seconds())
    
    if unit == "seconds":
        return total_seconds
    if unit == "minutes":
        return total_seconds / BASE_MINUTE
    if unit == "hours":
        return total_seconds / BASE_HOUR
    if unit == "days":
        return total_seconds / BASE_DAY
    if unit == "weeks":
        return total_seconds / (BASE_DAY * 7)
    raise ValueError("Unsupported unit")

def decompose_timedelta(dt1: datetime, dt2: datetime) -> dict:
    delta = abs(dt2 - dt1)
    total_seconds = int(delta.total_seconds())
    days = total_seconds // BASE_DAY
    remaining = total_seconds % BASE_DAY
    hours = remaining // BASE_HOUR
    remaining = remaining % BASE_HOUR
    minutes = remaining // BASE_MINUTE
    seconds = remaining % BASE_MINUTE
    return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == "__main__":
    start_dt = datetime(2023, 1, 1, 10, 30, 0)
    end_dt = datetime(2023, 1, 15, 14, 45, 30)
    
    result_seconds = calculate_time_difference(start_dt, end_dt, "seconds")
    print(result_seconds)
    
    result_days = calculate_time_difference(start_dt, end_dt, "days")
    print(result_days)
    
    breakdown = decompose_timedelta(start_dt, end_dt)
    print(breakdown)