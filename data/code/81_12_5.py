from datetime import datetime

def calculate_time_difference(start_datetime: str, end_datetime: str) -> float:
    time_format = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start_datetime, time_format)
    end_dt = datetime.strptime(end_datetime, time_format)
    time_diff = end_dt - start_dt
    hours_difference = time_diff.total_seconds() / 3600.0
    return hours_difference

if __name__ == '__main__':
    start = "2023-04-15 08:00:00"
    end = "2023-04-15 17:45:00"
    result = calculate_time_difference(start, end)
    print(result)