from datetime import datetime, timedelta

def calculate_remaining_fraction(year: int, month: int, day: int, hour: int, minute: int, second: int) -> float:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    if not (0 <= hour <= 23):
        raise ValueError("Hour must be between 0 and 23")
    if not (0 <= minute <= 59):
        raise ValueError("Minute must be between 0 and 59")
    if not (0 <= second <= 59):
        raise ValueError("Second must be between 0 and 59")

    start_dt = datetime(year, month, day, hour, minute, second)
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    days_in_month = {
        1: 31, 2: 29 if is_leap else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if day > days_in_month[month]:
        raise ValueError(f"Invalid day {day} for month {month} in year {year}")
    
    end_dt = start_dt + timedelta(days=days_in_month[month])
    
    now = datetime.now()
    
    if now < start_dt:
        return 1.0
    if now >= end_dt:
        return 0.0
    
    total_seconds = (end_dt - start_dt).total_seconds()
    elapsed_seconds = (now - start_dt).total_seconds()
    
    return 1.0 - (elapsed_seconds / total_seconds)

if __name__ == '__main__':
    result = calculate_remaining_fraction(2023, 1, 1, 0, 0, 0)
    print(result)