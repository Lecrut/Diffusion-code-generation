from datetime import date
DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return DAYS_IN_MONTH[month - 1]
if __name__ == '__main__':
    today = date.today()
    year, month = (today.year, today.month)
    last_day_of_month = days_in_month(year, month)
    days_left = (date(year, month, last_day_of_month) - today).days
    print(days_left)