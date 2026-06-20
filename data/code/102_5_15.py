import datetime

def is_weekday(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        weekday = date_obj.weekday()
        return 0 <= weekday < 5
    except ValueError:
        return False

if __name__ == '__main__':
    dates = ["2023-10-27", "2024-02-29", "2023-11-01", "2023-02-28"]
    weekday_dates = [date for date in dates if is_weekday(date)]
    print(weekday_dates)