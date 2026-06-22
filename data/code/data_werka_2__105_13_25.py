from datetime import date, timedelta

def find_next_weekend_date():
    today = date.today()
    weekday_index = today.weekday()
    
    if weekday_index == 5:
        return today
    if weekday_index == 6:
        return today
    
    days_to_saturday = 5 - weekday_index
    next_weekend = today + timedelta(days=days_to_saturday)
    
    if next_weekend < today:
        raise ValueError("Computed next weekend date is in the past")
    
    return next_weekend

if __name__ == '__main__':
    result = find_next_weekend_date()
    print(result)