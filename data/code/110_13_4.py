from datetime import datetime

def sort_iso_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ'))

if __name__ == '__main__':
    sample_dates = [
        '2023-01-01T00:00:00.000Z',
        '2022-12-31T23:59:59.999Z',
        '2023-01-02T00:00:00.000Z'
    ]
    sorted_dates = sort_iso_dates(sample_dates)
    print(sorted_dates)