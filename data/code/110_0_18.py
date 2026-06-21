from datetime import datetime

FORMAT_STRING = '%Y-%m-%d'
DEFAULT_DATES = [
    '2023-05-12',
    '2020-02-29',
    '2023-05-12',
    '2019-11-01',
    '2021-06-30'
]

def sort_chronologically(date_strings):
    def parse_date(date_str):
        return datetime.strptime(date_str, FORMAT_STRING)
    
    return sorted(date_strings, key=parse_date)

if __name__ == '__main__':
    unsorted = list(DEFAULT_DATES)
    sorted_dates = sort_chronologically(unsorted)
    print(sorted_dates)