from datetime import date
import calendar

MONTHS_IN_YEAR = 12

def subtract_months(target_date, months_to_subtract):
    year = target_date.year
    month = target_date.month
    day = target_date.day
    
    total_months = (year * MONTHS_IN_YEAR) + month - months_to_subtract
    
    new_year = total_months // MONTHS_IN_YEAR
    new_month = total_months % MONTHS_IN_YEAR
    
    if new_month == 0:
        new_month = MONTHS_IN_YEAR
        new_year -= 1
    
    max_days = calendar.monthrange(new_year, new_month)[1]
    new_day = min(day, max_days)
    
    return date(new_year, new_month, new_day)

if __name__ == '__main__':
    original_date = date(2023, 10, 15)
    result = subtract_months(original_date, 3)
    print(result)