from datetime import date, timedelta
import datetime

TARGET_WEEKDAY = 4

def find_next_target_date(current_date, target_weekday):
    if not isinstance(current_date, date) or not isinstance(target_weekday, int):
        raise ValueError("Invalid input types")
    if target_weekday < 0 or target_weekday > 6:
        raise ValueError("Target weekday out of range")
    
    days_ahead = target_weekday - current_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return current_date + timedelta(days=days_ahead)

def get_upcoming_friday(reference_date):
    if not isinstance(reference_date, date):
        raise TypeError("Reference date must be a date object")
    return find_next_target_date(reference_date, TARGET_WEEKDAY)

if __name__ == '__main__':
    ref_date = date(2023, 12, 15)
    next_friday = get_upcoming_friday(ref_date)
    print(next_friday.strftime("%Y-%m-%d"))