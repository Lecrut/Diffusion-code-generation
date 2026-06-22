from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def sort_dates_chronologically(date_strings):
    return sorted(date_strings, key=lambda d: datetime.strptime(d, DATE_FORMAT))

if __name__ == '__main__':
    sample_dates = ['2024-02-29', '2020-01-01', '2023-12-25', '2021-07-04', '2022-11-11']
    sorted_result = sort_dates_chronologically(sample_dates)
    print(sorted_result)