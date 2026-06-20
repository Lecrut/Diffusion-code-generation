import datetime
DATE_FORMAT = '%Y-%m-%d'

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid date format. Please use YYYY-MM-DD.')

def compare_dates(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    if date1 < date2:
        return date1
    elif date2 < date1:
        return date2
    else:
        raise ValueError('The dates are the same.')
if __name__ == '__main__':
    date1_input = '2023-10-25'
    date2_input = '2023-10-15'
    earlier_date = compare_dates(date1_input, date2_input)
    print(earlier_date)