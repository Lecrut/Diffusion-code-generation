import datetime

def is_weekend_optimized(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError('Input must be a datetime.date object')
    weekday = date_obj.weekday()
    return weekday >= 5
if __name__ == '__main__':
    try:
        date1 = datetime.date(2023, 10, 21)
        print(is_weekend_optimized(date1))
        date2 = datetime.date(2023, 10, 22)
        print(is_weekend_optimized(date2))
        date3 = datetime.date(2023, 10, 28)
        print(is_weekend_optimized(date3))
        date4 = datetime.date(2023, 10, 29)
        print(is_weekend_optimized(date4))
    except ValueError as e:
        print(e)