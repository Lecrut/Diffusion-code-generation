from datetime import date

def is_weekday(date_obj):
    if not isinstance(date_obj, date):
        raise TypeError("Input must be a datetime.date object")
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    print(is_weekday(sample_date))