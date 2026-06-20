from datetime import datetime

def elapsed_time_in_hours(start_time: str, end_time: str) -> float:
    time_format = "%Y-%m-%d %H:%M"
    
    try:
        start_dt = datetime.strptime(start_time, time_format)
        end_dt = datetime.strptime(end_time, time_format)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD HH:MM.") from e
    
    if start_dt > end_dt:
        raise ValueError("Start time cannot be later than end time.")
    
    time_difference = end_dt - start_dt
    return time_difference.total_seconds() / 3600.0

if __name__ == '__main__':
    try:
        start = "2023-10-01 09:00"
        end = "2023-10-01 17:30"
        result = elapsed_time_in_hours(start, end)
        print(result)
    except ValueError as e:
        print(e)