import datetime
DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month == 2 and is_leap_year(year):
        return 29
    return DAYS_IN_MONTH[month]

def calculate_remaining_days(current_date, target_month):
    current_year = current_date.year
    current_month = current_date.month
    remaining_days = sum((days_in_month(current_year, m) for m in range(current_month + 1, target_month)))
    if target_month == current_month:
        return 0
    remaining_days += days_in_month(current_year, target_month)
    return remaining_days
if __name__ == '__main__':
    sample_date = datetime.date(2023, 4, 15)
    target_month = 7
    print(calculate_remaining_days(sample_date, target_month))