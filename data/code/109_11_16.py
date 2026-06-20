import datetime

def is_valid_month(month):
    return 1 <= month <= 12

def days_in_month(year, month):
    if month == 2:
        return 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_time_remaining(target_month, target_day):
    if not is_valid_month(target_month):
        raise ValueError("Invalid month")
    
    today = datetime.date.today()
    year = today.year
    
    if target_month == today.month:
        days_left = days_in_month(year, target_month) - target_day + 1
    else:
        days_until_end_of_current_month = days_in_month(year, today.month) - today.day
        days_in_target_month = days_in_month(year, target_month)
        days_remaining = days_until_end_of_current_month + days_in_target_month - target_day + 1
    
    hours = (days_remaining * 24) // 60
    minutes = (days_remaining * 24 * 60) // 3600 % 60
    seconds = (days_remaining * 24 * 60 * 60) % 3600
    
    return hours, minutes, seconds

if __name__ == '__main__':
    target_month_1 = 10
    target_day_1 = 25
    print(calculate_time_remaining(target_month_1, target_day_1))