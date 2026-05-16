import datetime
def compare_datetimes_ignoring_time(dt1: datetime.datetime, dt2: datetime.datetime) -> bool:
    return dt1.date() == dt2.date()
if __name__ == '__main__':
    time1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    time2 = datetime.datetime(2023, 10, 26, 15, 45, 0)
    time3 = datetime.datetime(2023, 10, 27, 9, 0, 0)
    time4 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    print(f"Comparing {time1} and {time2}: {compare_datetimes_ignoring_time(time1, time2)}")
    print(f"Comparing {time1} and {time3}: {compare_datetimes_ignoring_time(time1, time3)}")
    print(f"Comparing {time1} and {time4}: {compare_datetimes_ignoring_time(time1, time4)}")
    print(f"Comparing {time2} and {time3}: {compare_datetimes_ignoring_time(time2, time3)}")