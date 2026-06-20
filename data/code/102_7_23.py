import calendar

def is_valid_date(date_obj):
    if not isinstance(date_obj, datetime.date):
        print('Invalid date object provided')
        return False
    return True

def is_weekday(date_obj):
    try:
        return date_obj.weekday() < 5
    except AttributeError:
        print('Invalid date object provided')
        return False

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    if is_valid_date(sample_date):
        print(is_weekday(sample_date))
    invalid_date = 'not a date'
    if is_valid_date(invalid_date):
        print(is_weekday(invalid_date))