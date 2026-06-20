from datetime import datetime

def sort_iso8601_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ'))

if __name__ == '__main__':
    sample_dates = [
        '2023-04-15T12:34:56.789Z',
        '2023-04-14T12:34:56.789Z',
        '2023-04-16T12:34:56.789Z'
    ]
    sorted_dates = sort_iso8601_dates(sample_dates)
    print(sorted_dates)