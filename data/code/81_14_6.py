import datetime
def calculate_duration_hours(start_time: datetime.datetime, end_time: datetime.datetime) -> float:
    duration = end_time - start_time
    duration_seconds = duration.total_seconds()
    duration_hours = duration_seconds / 3600.0
    return duration_hours
if __name__ == '__main__':
    time1 = datetime.datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime.datetime(2023, 1, 1, 12, 30, 15)
    result = calculate_duration_hours(time1, time2)
    print(result)