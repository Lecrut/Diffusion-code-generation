import pandas as pd

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        raise ValueError("Invalid month")

def remaining_days_in_month(date):
    dt = pd.to_datetime(date)
    days_left = days_in_month(dt.month, dt.year) - dt.day + 1
    return days_left

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(remaining_days_in_month(sample_date))