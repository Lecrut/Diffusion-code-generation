from datetime import datetime

def sort_iso_dates(date_list):
    return sorted(date_list, key=lambda date: datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z'))

if __name__ == '__main__':
    sample_dates = [
        '2023-10-05T14:30:00+00:00',
        '2023-09-01T08:00:00+00:00',
        '2023-11-15T16:45:00+00:00'
    ]
    sorted_dates = sort_iso_dates(sample_dates)
    print(sorted_dates)