from datetime import datetime
def calculate_duration_hours(dt1: datetime, dt2: datetime) -> float:
    diff = dt2 - dt1
    total_seconds = diff.total_seconds()
    hours = total_seconds / 3600.0
    return hours
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 3, 14, 30, 15)
    result = calculate_duration_hours(time1, time2)
    print(result)