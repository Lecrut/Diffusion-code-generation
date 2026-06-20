from datetime import datetime
DATE_FORMAT = '%Y-%m-%d'

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, DATE_FORMAT)
    except ValueError as e:
        print(f'Error parsing date {date_str}: {e}')
        raise

def compare_dates(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    if date1 < date2:
        return date_str1
    elif date1 > date2:
        return date_str2
    else:
        return 'Both dates are the same'
if __name__ == '__main__':
    earlier_date = compare_dates('2023-04-01', '2023-05-01')
    print(earlier_date)