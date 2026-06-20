import datetime

def has_weekday(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        weekday = date_obj.weekday()
        return 0 <= weekday <= 4
    except ValueError:
        return False

def check_dates(dates):
    results = {date: has_weekday(date) for date in dates}
    return results

if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2024-02-29",
        "2023-11-01",
        "2023-02-28"
    ]
    print(check_dates(sample_dates))