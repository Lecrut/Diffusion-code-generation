from datetime import datetime

def remaining_hours_in_month(year, month):
    if not (1 <= month <= 12) or not (1900 <= year <= 2100):
        raise ValueError("Invalid date")
    
    last_day = 31 if month in {1, 3, 5, 7, 8, 10, 12} else 30
    if month == 2:
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        last_day += 1 if is_leap_year else 0
    
    today = datetime(year, month, 1)
    remaining_days = last_day - today.day
    remaining_hours = remaining_days * 24
    
    return remaining_hours

if __name__ == '__main__':
    print(remaining_hours_in_month(2023, 4))