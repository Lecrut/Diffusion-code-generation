from datetime import datetime, timedelta

def calculate_time_diff(start_str: str, end_str: str) -> timedelta:
    fmt = "%Y-%m-%dT%H:%M:%S"
    if '.' in start_str:
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
    if '.' in end_str:
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
    
    start_dt = datetime.strptime(start_str, fmt)
    end_dt = datetime.strptime(end_str, fmt)
    
    return end_dt - start_dt

if __name__ == '__main__':
    start = "2023-10-01T10:00:00"
    end = "2023-10-01T12:30:45"
    result = calculate_time_diff(start, end)
    print(result)