import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_remaining_days(target_month, target_year):
    current_date = datetime.date.today()
    if target_year < current_date.year or (target_year == current_date.year and target_month < current_date.month):
        raise ValueError("Target date must be in the future")
    days_in_target_month = days_in_month(target_year, target_month)
    remaining_days = days_in_target_month - current_date.day
    return remaining_days

if __name__ == '__main__':
    target_month = 2
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)