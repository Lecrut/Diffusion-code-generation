import datetime
TARGET_YEAR = 2024

def find_first_sunday_after_jan_1():
    start_date = datetime.date(TARGET_YEAR, 1, 1)
    while start_date.weekday() != 6:
        start_date += datetime.timedelta(days=1)
    return start_date
if __name__ == '__main__':
    first_sunday = find_first_sunday_after_jan_1()
    print(first_sunday)