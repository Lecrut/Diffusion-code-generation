from datetime import datetime

def sort_iso8601_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.fromisoformat(date))

if __name__ == '__main__':
    sample_dates = [
        '2023-04-01T12:00:00Z',
        '2023-03-31T23:59:59Z',
        '2023-04-02T00:00:01Z'
    ]
    sorted_dates = sort_iso8601_dates(sample_dates)
    print(sorted_dates)