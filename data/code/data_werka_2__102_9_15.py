import datetime

def check_weekdays(dates):
    results = {}
    for date_str in dates:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        results[date_str] = dt.weekday() < 5
    return results

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    print(check_weekdays(sample_dates))