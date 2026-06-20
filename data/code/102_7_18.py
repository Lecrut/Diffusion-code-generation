import calendar

def is_valid_date_object(date_obj):
    return hasattr(date_obj, 'weekday')

def is_weekday(date_obj):
    if not is_valid_date_object(date_obj):
        print('Invalid date object provided')
        return False
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    print(is_weekday(sample_date))
    invalid_date = 'not a date'
    print(is_weekday(invalid_date))