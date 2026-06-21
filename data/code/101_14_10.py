import datetime
import calendar

def compute_weekday_for_date(year: int, month: int, day: int) -> str:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    
    target_date = datetime.date(year, month, day)
    weekday_index = target_date.weekday()
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    target_year = 2025
    target_month = 3
    target_day = 15
    result = compute_weekday_for_date(target_year, target_month, target_day)
    print(result)