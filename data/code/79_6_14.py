from datetime import datetime, timedelta

def next_month_date(date):
    year = date.year
    month = date.month
    day = date.day
    
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    
    try:
        return datetime(year, month, day)
    except ValueError:
        if month == 2 and day > 28:
            return datetime(year, month, 29) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else datetime(year, month, 28)
        elif month in [4, 6, 9, 11] and day > 30:
            return datetime(year, month, 30)
        else:
            raise

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 31)
    print(next_month_date(sample_date))