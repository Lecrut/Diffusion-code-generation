from datetime import datetime
def calculate_duration_hours(start_time: datetime, end_time: datetime) -> float:
    duration = end_time - start_time
    return duration.total_seconds() / 3600.0
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 1, 14, 30, 15)
    result = calculate_duration_hours(time1, time2)
    print(result)