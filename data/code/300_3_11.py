from datetime import date, timedelta
DAYS_PER_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_month(year, month):
    if month == 2:
        return DAYS_PER_MONTH[month] + (1 if is_leap_year(year) else 0)
    return DAYS_PER_MONTH[month]

def days_left_in_month():
    today = date.today()
    last_day_of_month = date(today.year, today.month, days_in_month(today.year, today.month))
    return (last_day_of_month - today).days
if __name__ == '__main__':
    print(days_left_in_month())