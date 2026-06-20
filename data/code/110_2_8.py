from datetime import datetime

def sort_iso_dates(date_list):
    return sorted(date_list, key=lambda date: datetime.strptime(date, '%Y-%m-%dT%H:%M:%S'))

if __name__ == '__main__':
    sample_dates = [
        '2023-10-05T14:30:00',
        '2023-09-28T09:15:00',
        '2023-10-01T12:45:00'
    ]
    sorted_dates = sort_iso_dates(sample_dates)
    print(sorted_dates)