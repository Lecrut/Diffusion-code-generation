import datetime

def get_day_of_month(dates):
    results = []
    for date_str in dates:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        results.append(dt.day)
    return results

if __name__ == '__main__':
    dates = ["2023-10-01", "2023-10-15", "2023-10-31"]
    days = get_day_of_month(dates)
    print(days)