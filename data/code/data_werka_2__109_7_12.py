import calendar
import datetime

def compute_remaining_seconds_in_month(year=None, month=None):
    if year is None:
        year = datetime.datetime.now().year
    if month is None:
        month = datetime.datetime.now().month
    
    if not 1 <= month <= 12:
        raise ValueError(f"Invalid month: {month}")
    if not 1582 <= year:
        raise ValueError(f"Invalid year: {year}")
    
    last_day = calendar.monthrange(year, month)[1]
    last_second = datetime.datetime(year, month, last_day, 23, 59, 59)
    now = datetime.datetime.now()
    
    if now.year > year or (now.year == year and now.month > month):
        return 0
    
    delta = last_second - now
    seconds = delta.days * 86400 + delta.seconds
    
    return max(seconds, 0)

if __name__ == '__main__':
    result = compute_remaining_seconds_in_month(2024, 10)
    print(result)