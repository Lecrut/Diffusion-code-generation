import datetime

def validate_dates(dt1, dt2):
    if not isinstance(dt1, datetime.datetime) or not isinstance(dt2, datetime.datetime):
        raise ValueError("Both arguments must be instances of datetime.datetime")
    if dt1.tzinfo is None and dt2.tzinfo is None:
        return
    if dt1.tzinfo != dt2.tzinfo:
        raise ValueError("Dates must have the same timezone or neither should have one")

def calculate_time_difference(dt1, dt2):
    validate_dates(dt1, dt2)
    difference = dt1 - dt2
    return difference

if __name__ == '__main__':
    time1 = datetime.datetime(2023, 1, 1, 10, 0, 0, tzinfo=datetime.timezone.utc)
    time2 = datetime.datetime(2022, 1, 1, 10, 0, 0, tzinfo=datetime.timezone.utc)
    time3 = datetime.datetime(2023, 1, 1, 11, 0, 0, tzinfo=datetime.timezone.utc)

    diff1 = calculate_time_difference(time2, time1)
    print(f"Difference between time1 and time2: {diff1}")

    diff2 = calculate_time_difference(time3, time1)
    print(f"Difference between time1 and time3: {diff2}")