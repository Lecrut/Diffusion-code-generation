import datetime

def calculate_time_remaining(target_month, target_day):
    today = datetime.date.today()
    year = today.year
    
    if target_year < year or (target_year == year and target_month < today.month) or (target_year == year and target_month == today.month and target_day <= today.day):
        raise ValueError("Target date is in the past or today.")
    
    days_in_target_month = 31 if target_month in [1, 3, 5, 7, 8, 10, 12] else 30
    if target_month == 2:
        days_in_target_month = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    
    remaining_days = (datetime.date(year, target_month, target_day) - today).days
    hours_remaining = remaining_days * 24
    minutes_remaining = hours_remaining * 60
    seconds_remaining = minutes_remaining * 60
    
    return hours_remaining, minutes_remaining, seconds_remaining

if __name__ == '__main__':
    target_month_1 = 10
    target_day_1 = 25
    print(calculate_time_remaining(2023, target_month_1, target_day_1))