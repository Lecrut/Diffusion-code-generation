import datetime

weekend_days = {5: 'Weekend', 6: 'Weekend'}

def is_weekend_optimized(date_obj):
    weekday = date_obj.weekday()
    return weekend_days.get(weekday, 'Weekday')

if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 1)
    print(is_weekend_optimized(date1))
    date2 = datetime.date(2023, 10, 8)
    print(is_weekend_optimized(date2))
    date3 = datetime.date(2023, 10, 9)
    print(is_weekend_optimized(date3))