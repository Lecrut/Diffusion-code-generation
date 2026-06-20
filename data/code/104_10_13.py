import datetime

def validate_date(date):
    if not isinstance(date, datetime.date):
        raise TypeError('Input must be of type datetime.date')

def compare_dates(date1, date2):
    validate_date(date1)
    validate_date(date2)
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0
if __name__ == '__main__':
    try:
        result = compare_dates(datetime.date(2023, 4, 1), datetime.date(2023, 4, 15))
        print(result)
    except Exception as e:
        print(e)