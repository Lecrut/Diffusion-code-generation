from datetime import datetime
def calculate_time_difference(dt1: datetime, dt2: datetime) -> datetime:
    if dt2 > dt1:
        return dt2 - dt1
    else:
        return dt1 - dt2
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 1, 10, 30, 0)
    difference1 = calculate_time_difference(time1, time2)
    print(f"Difference between {time1} and {time2}: {difference1}")
    time3 = datetime(2023, 1, 1, 15, 0, 0)
    time4 = datetime(2023, 1, 1, 12, 0, 0)
    difference2 = calculate_time_difference(time3, time4)
    print(f"Difference between {time3} and {time4}: {difference2}")