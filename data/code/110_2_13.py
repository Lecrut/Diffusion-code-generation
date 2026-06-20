from datetime import datetime

def sort_iso8601_dates(date_list):
    return sorted(date_list, key=lambda date: datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z'))

if __name__ == '__main__':
    sample_dates = [
        '2023-04-15T12:30:00+00:00',
        '2023-04-14T18:45:00+00:00',
        '2023-04-16T09:15:00+00:00'
    ]
    sorted_dates = sort_iso8601_dates(sample_dates)
    print(sorted_dates)