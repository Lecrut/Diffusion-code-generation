import datetime

WEEKDAY_THRESHOLD = 5

def is_weekday(date_obj):
    return date_obj.weekday() < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 10, 23),
        datetime.datetime(2023, 10, 24),
        datetime.datetime(2023, 10, 25),
        datetime.datetime(2023, 10, 26),
        datetime.datetime(2023, 10, 27),
        datetime.datetime(2023, 10, 28),
        datetime.datetime(2023, 10, 29)
    ]

    for date in sample_dates:
        print(is_weekday(date))