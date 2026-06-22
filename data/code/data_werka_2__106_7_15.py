from datetime import date

MONTH_DAYS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def calculate_full_years(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    
    years = end_date.year - start_date.year
    
    if years == 0:
        return 0
    
    current_year = start_date.year
    current_month = start_date.month
    current_day = start_date.day
    
    for _ in range(years):
        next_year = current_year + 1
        days_in_current_year = 366 if current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0) else 365
        
        days_left_in_current_month = MONTH_DAYS[current_month] - current_day
        if current_month == 2 and days_in_current_year == 366:
            days_left_in_current_month += 1
        
        days_in_full_months = 0
        month = current_month + 1
        while month <= 12:
            days_in_full_months += MONTH_DAYS[month]
            month += 1
        
        days_until_anniversary = days_left_in_current_month + days_in_full_months
        
        if days_until_anniversary > days_in_current_year:
            break
            
        if days_until_anniversary > (end_date - date(current_year, current_month, current_day)).days:
            break
            
        current_year += 1
        current_month = start_date.month
        current_day = start_date.day
        
    return current_year - start_date.year

if __name__ == '__main__':
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    result = calculate_full_years(start, end)
    print(result)