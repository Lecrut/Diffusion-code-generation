from datetime import date

DAYS_PER_YEAR = 365
DAYS_PER_LEAP_YEAR = 366

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    else:
        return 29 if is_leap_year(year) else 28

def days_between_dates(date1, date2):
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be instances of date.")
    
    start_date = min(date1, date2)
    end_date = max(date1, date2)
    
    total_days = 0
    current_year = start_date.year
    
    while current_year < end_date.year:
        if is_leap_year(current_year):
            total_days += DAYS_PER_LEAP_YEAR
        else:
            total_days += DAYS_PER_YEAR
        current_year += 1
    
    for month in range(start_date.month, end_date.month + 1):
        if month == start_date.month and month == end_date.month:
            total_days += (end_date.day - start_date.day)
        elif month == start_date.month:
            total_days += days_in_month(current_year, month) - start_date.day
        elif month == end_date.month:
            total_days += end_date.day
        else:
            total_days += days_in_month(current_year, month)
    
    return abs(total_days)

if __name__ == '__main__':
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 15)
    print(days_between_dates(date1, date2))