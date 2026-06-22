from datetime import date, timedelta
import calendar

def get_next_weekend_date():
    today = date.today()
    current_weekday = today.weekday()
    
    if current_weekday == 5:
        next_saturday = today
    elif current_weekday == 6:
        next_saturday = today
    else:
        days_until_saturday = 5 - current_weekday
        next_saturday = today + timedelta(days=days_until_saturday)
        
    if next_saturday < today:
        raise ValueError("Logic error: next_saturday cannot be before today")
        
    return next_saturday

if __name__ == '__main__':
    result = get_next_weekend_date()
    print(result)