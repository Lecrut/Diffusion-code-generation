from datetime import date

def is_valid_date(date_obj):
    if not isinstance(date_obj, date):
        raise TypeError("Input must be of type 'date'")
    return True

def years_between_dates(date1: date, date2: date) -> int:
    is_valid_date(date1)
    is_valid_date(date2)
    delta = abs((date2 - date1).days)
    return delta // 365

if __name__ == '__main__':
    d1 = date(2010, 1, 1)
    d2 = date(2023, 4, 15)
    print(years_between_dates(d1, d2))