from datetime import datetime, timedelta

def calculate_time_diff(start_str: str, end_str: str) -> timedelta:
    fmt = "%Y-%m-%dT%H:%M:%S"
    start_dt = datetime.strptime(start_str, fmt)
    end_dt = datetime.strptime(end_str, fmt)
    return end_dt - start_dt

if __name__ == '__main__':
    result = calculate_time_diff("2023-01-01T10:00:00", "2023-01-01T12:30:00")
    print(result)