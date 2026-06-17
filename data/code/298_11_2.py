import datetime
if __name__ == '__main__':
    time1 = datetime.datetime(2023, 10, 27, 10, 30, 0)
    time2 = datetime.datetime(2023, 10, 27, 11, 45, 15)
    time_difference = abs(time2 - time1)
    total_seconds = time_difference.total_seconds()
    print(total_seconds)