from datetime import date, timedelta
import calendar

def get_next_seven_day_marker(start_date: date = None) -> date:
    if start_date is None:
        start_date = date(2024, 1, 1)
    
    if not isinstance(start_date, date):
        raise ValueError("start_date must be a date instance")
    
    if start_date.year < 1 or start_date.year > 9999:
        raise ValueError("Year out of range")
        
    days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
    
    if start_date.day > days_in_month:
        raise ValueError("Invalid day for month")
        
    target_days = 7
    next_date = start_date + timedelta(days=target_days)
    
    return next_date

if __name__ == '__main__':
    start = date(2024, 1, 1)
    result = get_next_seven_day_marker(start)
    print(result)