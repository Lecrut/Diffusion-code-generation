from datetime import datetime

def sort_dates(date_strings):
    if not date_strings:
        return []
    return sorted(date_strings, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01']
    print(sort_dates(sample_dates))