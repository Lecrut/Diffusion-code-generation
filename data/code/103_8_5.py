import datetime
if __name__ == '__main__':
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = now - start_of_day
    print(f"Current time: {now}")
    print(f"Start of the day: {start_of_day}")
    print(f"Difference (timedelta): {time_difference}")
    print(f"Difference in seconds: {time_difference.total_seconds()}")