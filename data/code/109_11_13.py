import datetime

def calculate_time_remaining(target_month, target_day):
    today = datetime.date.today()
    year = today.year
    
    if target_month > today.month:
        next_year = year + (target_month - today.month) // 12
        remaining_months = (target_month - today.month) % 12
        last_day_of_current_month = today.replace(day=28) + datetime.timedelta(days=4)
        days_in_last_month = last_day_of_current_month.day
        
        total_days_passed = sum((datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days for month in range(today.month))
        total_days_remaining = (365 if next_year % 4 != 0 else 366) * (next_year - year - 1)
        
        days_in_target_month = target_day
        
        time_remaining = datetime.timedelta(days=total_days_passed + total_days_remaining + days_in_last_month - target_day)
    elif target_month == today.month:
        if target_day > today.day:
            days_in_current_month = (datetime.date(year, target_month + 1, 1) - datetime.date(year, target_month, 1)).days
            time_remaining = datetime.timedelta(days=days_in_current_month - target_day)
        else:
            time_remaining = datetime.timedelta(0)
    else:
        next_year = year + (target_month - today.month) // 12
        remaining_months = (target_month - today.month) % 12
        
        total_days_passed = sum((datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days for month in range(today.month))
        total_days_remaining = (365 if next_year % 4 != 0 else 366) * remaining_months
        
        days_in_target_month = target_day
        
        time_remaining = datetime.timedelta(days=total_days_passed + total_days_remaining - target_day)
    
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    target_month_1 = 4
    target_day_1 = 15
    print(calculate_time_remaining(target_month_1, target_day_1))