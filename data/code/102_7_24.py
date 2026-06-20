import calendar

def is_weekday(date_obj):
    try:
        return date_obj.weekday() < 5
    except AttributeError:
        return False
if __name__ == '__main__':
    from datetime import date
    sample_date = date(2023, 10, 5)
    print(is_weekday(sample_date))
    sample_date = date(2023, 10, 6)
    print(is_weekday(sample_date))
    sample_date = 'not a date'
    print(is_weekday(sample_date))