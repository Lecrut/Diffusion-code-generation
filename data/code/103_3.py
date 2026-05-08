if __name__ == '__main__':
    import datetime
    now = datetime.datetime(2023, 10, 27, 14, 30, 0)
    start_of_day = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
    difference = now - start_of_day
    print(difference)