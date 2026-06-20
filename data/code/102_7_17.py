import calendar

def is_weekday(date_obj):
    try:
        return date_obj.weekday() < 5
    except AttributeError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    from datetime import datetime
    sample_date = datetime(2023, 10, 5)
    print(is_weekday(sample_date))
    sample_date = datetime(2023, 10, 6)
    print(is_weekday(sample_date))
    invalid_date = 'not a date'
    print(is_weekday(invalid_date))