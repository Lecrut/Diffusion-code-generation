from datetime import datetime

def sort_iso_dates(dates):
    return sorted(dates, key=lambda date: datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z'))

if __name__ == '__main__':
    sample_dates = [
        '2023-01-01T00:00:00+00:00',
        '2022-12-31T23:59:59+00:00',
        '2023-01-02T00:01:00+00:00'
    ]
    sorted_dates = sort_iso_dates(sample_dates)
    print(sorted_dates)