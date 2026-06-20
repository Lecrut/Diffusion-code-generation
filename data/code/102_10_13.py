import datetime

def is_weekday(date_obj):
    weekday = date_obj.weekday()
    return 0 <= weekday < 5

if __name__ == '__main__':
    test_dates = [
        datetime.datetime(2023, 10, 23),
        datetime.datetime(2023, 10, 24),
        datetime.datetime(2023, 10, 25),
        datetime.datetime(2023, 10, 26),
        datetime.datetime(2023, 10, 27),
        datetime.datetime(2023, 10, 28),
        datetime.datetime(2023, 10, 29)
    ]

    for date in test_dates:
        print(is_weekday(date))