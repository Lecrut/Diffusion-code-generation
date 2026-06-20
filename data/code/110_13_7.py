from datetime import datetime
ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

def sort_iso_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.strptime(date, ISO_FORMAT))
if __name__ == '__main__':
    sample_dates = ['2023-01-01T12:00:00Z', '2022-12-31T23:59:59Z', '2023-01-02T00:00:00Z']
    sorted_dates = sort_iso_dates(sample_dates)
    print(sorted_dates)