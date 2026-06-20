import datetime
DATE_FORMATS = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y', '%Y/%m/%d']

def parse_date(date_string):
    for fmt in DATE_FORMATS:
        try:
            return datetime.datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    raise ValueError('Date format not recognized')

def calculate_date_difference(date_string1, date_string2):
    date1 = parse_date(date_string1)
    date2 = parse_date(date_string2)
    return abs((date1 - date2).days)
if __name__ == '__main__':
    result = calculate_date_difference('2023-01-01', '01/02/2023')
    print(result)