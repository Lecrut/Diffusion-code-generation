import datetime

def get_remaining_minutes_in_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    last_day = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month != 2 else 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    end_of_month = datetime.datetime(year, month, last_day, 23, 59, 59)
    remaining_seconds = (end_of_month - now).total_seconds()
    remaining_minutes = int(remaining_seconds // 60)
    return remaining_minutes

if __name__ == '__main__':
    result = get_remaining_minutes_in_month()
    print(result)