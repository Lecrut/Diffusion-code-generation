import datetime

WEEKEND_DAYS = {0, 6}

def is_weekday(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.weekday() not in WEEKEND_DAYS

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    results = {d: is_weekday(d) for d in sample_dates}
    print(results)