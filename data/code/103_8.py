import datetime
if __name__ == '__main__':
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = now - start_of_day
    print(f"Current Time: {now}")
    print(f"Start of Day: {start_of_day}")
    print(f"Difference (Time Elapsed): {time_difference}")