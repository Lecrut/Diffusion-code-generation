from datetime import datetime

def validate_datetime_format(dt_str):
    time_format = "%Y-%m-%d %H:%M:%S"
    try:
        datetime.strptime(dt_str, time_format)
        return True
    except ValueError:
        return False

def elapsed_time_in_hours(start_time: str, end_time: str) -> float:
    if not (validate_datetime_format(start_time) and validate_datetime_format(end_time)):
        raise ValueError("Invalid datetime format. Expected '%Y-%m-%d %H:%M:%S'")
    
    start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    time_difference = end_dt - start_dt
    return time_difference.total_seconds() / 3600.0

if __name__ == '__main__':
    start = "2023-01-01 12:00:00"
    end = "2023-01-01 14:30:00"
    result = elapsed_time_in_hours(start, end)
    print(result)