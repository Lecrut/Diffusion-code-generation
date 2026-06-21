from datetime import datetime

def group_dates_by_month(dates):
    grouped = {}
    for date in dates:
        year_month = date.strftime('%Y-%m')
        if year_month not in grouped:
            grouped[year_month] = []
        grouped[year_month].append(date)
    return grouped

if __name__ == '__main__':
    sample_dates = [
        datetime(2023, 1, 15),
        datetime(2023, 2, 20),
        datetime(2023, 1, 25),
        datetime(2024, 1, 10)
    ]
    result = group_dates_by_month(sample_dates)
    print(result)