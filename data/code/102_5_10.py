import datetime

WEEKDAY_THRESHOLD = 4

def is_weekday(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    return date_obj.weekday() <= WEEKDAY_THRESHOLD

if __name__ == '__main__':
    dates = [
        "2023-10-27",
        "2024-02-29",
        "2023-10-28",
        "2023-02-28"
    ]
    print([is_weekday(date) for date in dates])