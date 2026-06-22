import datetime

def is_weekend_optimized(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        weekday = date_obj.weekday()
        return weekend if weekday >= 5 else weekday
    except ValueError:
        raise ValueError("Invalid date format or out of valid range")

if __name__ == '__main__':
    date1 = (2023, 10, 1)
    print(is_weekend_optimized(*date1))
    date2 = (2023, 10, 8)
    print(is_weekend_optimized(*date2))
    date3 = (2023, 10, 9)
    print(is_weekend_optimized(*date3))