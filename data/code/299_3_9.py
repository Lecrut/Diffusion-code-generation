import datetime

def is_weekend_optimized(date_obj):
    weekday = date_obj.weekday()
    return weekday >= 5
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 21)
    print(is_weekend_optimized(date1))
    date2 = datetime.date(2023, 10, 22)
    print(is_weekend_optimized(date2))