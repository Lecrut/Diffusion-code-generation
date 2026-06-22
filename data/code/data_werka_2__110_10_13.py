from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

def sort_dates(date_strings):
    if not date_strings:
        return []
    date_map = {
        'year': lambda d: int(d[0:4]),
        'month': lambda d: int(d[5:7]),
        'day': lambda d: int(d[8:10])
    }
    def parse_key(d):
        return (date_map['year'](d), date_map['month'](d), date_map['day'](d))
    return sorted(date_strings, key=parse_key)

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01']
    result = sort_dates(sample_dates)
    print(result)