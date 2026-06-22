import datetime

WEEKEND_DAYS = {5: True, 6: True}

def is_weekend_optimized(date_obj):
    weekday = date_obj.weekday()
    return WEEKEND_DAYS.get(weekday, False)

if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 1)
    print(is_weekend_optimized(date1))
    
    date2 = datetime.date(2023, 10, 8)
    print(is_weekend_optimized(date2))
    
    date3 = datetime.date(2023, 10, 9)
    print(is_weekend_optimized(date3))