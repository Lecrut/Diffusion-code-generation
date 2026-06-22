from datetime import date

DAYS_IN_COMMON_YEAR = 365
DAYS_IN_LEAP_YEAR = 366

def compute_absolute_year_gap(first_date: date, second_date: date) -> int:
    if not isinstance(first_date, date) or not isinstance(second_date, date):
        raise ValueError("Inputs must be datetime.date objects")
    
    delta = second_date - first_date
    total_days = abs(delta.days)
    
    years_count = 0
    current_date = first_date
    
    while total_days > 0:
        if current_date.year % 4 == 0:
            if current_date.year % 100 == 0:
                if current_date.year % 400 == 0:
                    days_in_year = DAYS_IN_LEAP_YEAR
                else:
                    days_in_year = DAYS_IN_COMMON_YEAR
            else:
                days_in_year = DAYS_IN_LEAP_YEAR
        else:
            days_in_year = DAYS_IN_COMMON_YEAR
        
        remaining_days = total_days - days_in_year
        
        if remaining_days < 0:
            break
        
        total_days = remaining_days
        current_date = date(current_date.year + 1, current_date.month, current_date.day)
        years_count += 1
        
    return years_count

if __name__ == '__main__':
    start = date(2020, 3, 1)
    end = date(2025, 3, 1)
    gap = compute_absolute_year_gap(start, end)
    print(gap)