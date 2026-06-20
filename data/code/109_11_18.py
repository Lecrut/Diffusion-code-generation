import datetime

def calculate_remaining_time(target_month, target_day):
    today = datetime.date.today()
    year = today.year
    
    if not (1 <= target_month <= 12) or not (1 <= target_day <= 31):
        raise ValueError("Invalid month or day")
    
    if target_month == today.month:
        if target_day > today.day:
            end_of_month = datetime.date(year, today.month, 1) + datetime.timedelta(days=31)
            remaining_time = end_of_month - today
        else:
            remaining_time = datetime.timedelta(0)
    else:
        next_month = target_month + 1
        if next_month > 12:
            next_month = 1
            year += 1
        
        first_day_of_target_month = datetime.date(year, target_month, 1)
        end_of_month = first_day_of_target_month.replace(day=first_day_of_target_month.month) + datetime.timedelta(days=31)
        
        remaining_time = end_of_month - today
    
    hours, remainder = divmod(remaining_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

if __name__ == '__main__':
    target_month_1 = 10
    target_day_1 = 25
    print(calculate_remaining_time(target_month_1, target_day_1))