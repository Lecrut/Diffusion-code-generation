import datetime

def is_weekend_optimized(date_obj):
    weekday = date_obj.weekday()
    return weekday >= 5

if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 1),
        datetime.date(2023, 10, 8),
        datetime.date(2023, 10, 9)
    ]
    
    for date in sample_dates:
        print(is_weekend_optimized(date))