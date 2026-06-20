from datetime import datetime

def sort_iso_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.fromisoformat(date))

if __name__ == '__main__':
    sample_dates = [
        '2023-10-05T16:30:00Z',
        '2023-08-25T14:45:00Z',
        '2023-09-10T09:00:00Z'
    ]
    sorted_dates = sort_iso_dates(sample_dates)
    print(sorted_dates)