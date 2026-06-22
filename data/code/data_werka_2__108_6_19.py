import datetime

def get_day_of_month(dates):
    results = []
    for date_str in dates:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        results.append(dt.day)
    return results

if __name__ == '__main__':
    dates = ["2023-10-05", "2024-02-29", "2025-12-31"]
    days = get_day_of_month(dates)
    print(days)