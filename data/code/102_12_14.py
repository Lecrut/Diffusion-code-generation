from datetime import date

def is_weekday(date_obj):
    if not isinstance(date_obj, date):
        raise TypeError('Input must be a date object')
    return date_obj.weekday() < 5
if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    print(is_weekday(sample_date))
    sample_date = date(2023, 10, 6)
    print(is_weekday(sample_date))
    sample_date = date(2023, 10, 7)
    print(is_weekday(sample_date))
    sample_date = date(2023, 10, 8)
    print(is_weekday(sample_date))
    sample_date = date(2023, 10, 9)
    print(is_weekday(sample_date))
    sample_date = date(2023, 10, 10)
    print(is_weekday(sample_date))
    sample_date = date(2023, 10, 11)
    print(is_weekday(sample_date))