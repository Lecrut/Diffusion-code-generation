from datetime import datetime
def calculate_duration_hours(start_time: datetime, end_time: datetime) -> float:
    time_difference = end_time - start_time
    duration_hours = time_difference.total_seconds() / 3600.0
    return duration_hours
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 1, 13, 30, 0)
    result = calculate_duration_hours(time1, time2)
    print(result)