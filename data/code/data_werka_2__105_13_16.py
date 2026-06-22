from datetime import date, timedelta

WEEKDAY_SATURDAY = 5
WEEKDAY_SUNDAY = 6
WEEKEND_DAYS = {WEEKDAY_SATURDAY, WEEKDAY_SUNDAY}

def find_next_weekend_date():
    today = date.today()
    current_weekday = today.weekday()
    
    if current_weekday in WEEKEND_DAYS:
        return today
    
    days_ahead = 1
    next_date = today + timedelta(days=days_ahead)
    
    while next_date.weekday() not in WEEKEND_DAYS:
        days_ahead += 1
        next_date = today + timedelta(days=days_ahead)
        
    return next_date

if __name__ == '__main__':
    result = find_next_weekend_date()
    print(result)