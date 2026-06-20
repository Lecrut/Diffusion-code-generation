from datetime import datetime

def sort_iso8601_dates(date_list):
    try:
        return sorted(date_list, key=lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z"))
    except ValueError as e:
        raise ValueError("Invalid ISO 8601 date format") from e

if __name__ == '__main__':
    sample_dates = [
        '2023-04-01T12:00:00+00:00',
        '2023-03-31T23:59:59+00:00',
        '2023-04-02T00:00:00+00:00'
    ]
    sorted_dates = sort_iso8601_dates(sample_dates)
    print(sorted_dates)