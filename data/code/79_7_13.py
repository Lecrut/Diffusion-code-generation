from datetime import date, timedelta

def next_month(date):
    year = date.year
    month = date.month
    day = date.day
    
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    
    try:
        return date(year, month, day)
    except ValueError:
        if month == 2 and day > 28:
            return date(year, month, 29)
        elif month in [4, 6, 9, 11] and day > 30:
            return date(year, month, 30)
        else:
            raise ValueError("Invalid date")

if __name__ == '__main__':
    sample_date = date(2023, 10, 31)
    print(next_month(sample_date))