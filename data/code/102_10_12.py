import datetime
from calendar import isoweekday

WEEKDAY_THRESHOLD = 5

def is_weekday(date_obj):
    return isoweekday(date_obj.date()) < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    sample_dates = [
        "2023-10-23",
        "2023-10-24",
        "2023-10-25",
        "2023-10-26",
        "2023-10-27",
        "2023-10-28",
        "2023-10-29"
    ]

    for date_str in sample_dates:
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            print(is_weekday(date_obj))
        except ValueError:
            print(False)