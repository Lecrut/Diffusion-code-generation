from datetime import date, timedelta

FIRST_DAY = 1
LAST_DAY = 31
MONTHS_IN_YEAR = 12
TIMEDELTA_DAYS = 1

def calculate_days_remaining(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= LAST_DAY):
        raise ValueError("Day must be valid for the given month")
    
    if month == MONTHS_IN_YEAR:
        next_month_start = date(year + 1, FIRST_DAY, FIRST_DAY)
    else:
        next_month_start = date(year, month + FIRST_DAY, FIRST_DAY)
    
    last_day_of_current_month = next_month_start - timedelta(days=TIMEDELTA_DAYS)
    
    if day > last_day_of_current_month.day:
        raise ValueError("Day exceeds days in month")
        
    current_date = date(year, month, day)
    remaining = (last_day_of_current_month - current_date).days + 1
    return remaining

if __name__ == '__main__':
    result = calculate_days_remaining(2023, 10, 15)
    print(result)
    result2 = calculate_days_remaining(2024, 2, 20)
    print(result2)
    result3 = calculate_days_remaining(2023, 12, 31)
    print(result3)