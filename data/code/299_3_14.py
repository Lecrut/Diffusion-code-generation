import datetime

def is_weekend_optimized(date):
    if not isinstance(date, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    
    weekday = date.weekday()
    return weekday >= 5

if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 1)
    print(is_weekend_optimized(date1))
    date2 = datetime.date(2023, 10, 8)
    print(is_weekend_optimized(date2))
    date3 = datetime.date(2023, 10, 9)
    print(is_weekend_optimized(date3))