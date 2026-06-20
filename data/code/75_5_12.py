import datetime
DAYS_PER_YEAR = 365
DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return DAYS_PER_MONTH[month - 1]

def calculate_date_difference(date1, date2):
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    day_diff = date2.day - date1.day
    total_days = 0
    for month in range(1, date1.month):
        total_days += days_in_month(date1.year, month)
    total_days += date1.day
    for month in range(date2.month + 1, 13):
        total_days -= days_in_month(date2.year, month)
    total_days -= date2.day
    total_days += year_diff * DAYS_PER_YEAR
    if is_leap_year(date2.year) and (not is_leap_year(date1.year)):
        total_days += date2.year - date1.year
    if month_diff > 0:
        for month in range(1, month_diff + 1):
            total_days += days_in_month(date1.year + year_diff, month)
    else:
        for month in range(month_diff + 1, 0):
            total_days -= days_in_month(date1.year + year_diff, month)
    return abs(total_days)
if __name__ == '__main__':
    date1 = datetime.date(2020, 5, 15)
    date2 = datetime.date(2023, 12, 25)
    print(calculate_date_difference(date1, date2))