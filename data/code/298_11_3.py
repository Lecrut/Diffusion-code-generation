import datetime
if __name__ == '__main__':
    dt1 = datetime.datetime(2023, 10, 27, 10, 30, 0)
    dt2 = datetime.datetime(2023, 10, 27, 11, 45, 15)
    time_difference = abs(dt2 - dt1)
    total_seconds = time_difference.total_seconds()
    print(total_seconds)