import datetime

DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_last_day_of_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return DAYS_IN_MONTH[month]

def calculate_remaining_days(target_month, target_year):
    today = datetime.date.today()
    if target_year < today.year or (target_year == today.year and target_month <= today.month):
        raise ValueError("Invalid date input")
    
    last_day_of_current_month = get_last_day_of_month(today.year, today.month)
    days_passed_in_current_month = today.day
    
    days_remaining_in_current_month = last_day_of_current_month - days_passed_in_current_month
    days_passed_in_target_month = 0
    
    if target_year == today.year:
        days_passed_in_target_month = (datetime.date(target_year, target_month, 1) - datetime.date(today.year, today.month + 1, 1)).days
    
    remaining_days = days_remaining_in_current_month + days_passed_in_target_month
    return remaining_days

if __name__ == '__main__':
    target_month = 2
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)