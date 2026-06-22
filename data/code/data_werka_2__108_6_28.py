import datetime

def get_day_of_month(dates):
    results = []
    for date_str in dates:
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        results.append(dt.day)
    return results

if __name__ == '__main__':
    sample_dates = ["2023-10-15", "2024-02-29", "2021-01-01"]
    days = get_day_of_month(sample_dates)
    print(days)