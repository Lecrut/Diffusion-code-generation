from datetime import datetime

_DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year: int, month: int) -> int:
    if month == 2 and is_leap_year(year):
        return 29
    return _DAYS_IN_MONTH[month]

def calculate_remaining_fraction(year: int, month: int, day: int, hour: int, minute: int, second: int) -> float:
    now = datetime.now()
    
    if now.year < year or (now.year == year and now.month < month) or \
       (now.year == year and now.month == month and now.day < day):
        return 1.0
    
    if now.year > year or (now.year == year and now.month > month) or \
       (now.year == year and now.month == month and now.day > day):
        return 0.0
    
    current_date = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    start_date = datetime(year, month, day, hour, minute, second)
    next_month_start = datetime(year, month + 1, 1) if month < 12 else datetime(year + 1, 1, 1)
    
    total_seconds_in_month = (next_month_start - start_date).total_seconds()
    elapsed_seconds = (current_date - start_date).total_seconds()
    
    if total_seconds_in_month == 0:
        return 0.0
        
    return 1.0 - (elapsed_seconds / total_seconds_in_month)

if __name__ == '__main__':
    start_year, start_month, start_day = 2023, 1, 1
    end_year, end_month, end_day = 2023, 2, 1
    
    result = calculate_remaining_fraction(start_year, start_month, start_day, 0, 0, 0)
    print(f"Remaining fraction: {result}")
    
    future_year, future_month, future_day = 2024, 5, 15
    future_result = calculate_remaining_fraction(future_year, future_month, future_day, 10, 30, 0)
    print(f"Future remaining fraction: {future_result}")