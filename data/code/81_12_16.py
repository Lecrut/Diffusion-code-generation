from datetime import datetime

def calculate_elapsed_hours(start_time: str, end_time: str) -> float:
    time_format = "%Y-%m-%d %H:%M"
    start_dt = datetime.strptime(start_time, time_format)
    end_dt = datetime.strptime(end_time, time_format)
    time_difference = end_dt - start_dt
    return time_difference.total_seconds() / 3600.0

if __name__ == '__main__':
    start = "2023-01-01 09:00"
    end = "2023-01-01 17:30"
    result = calculate_elapsed_hours(start, end)
    print(result)