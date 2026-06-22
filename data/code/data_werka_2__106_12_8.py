from datetime import date
import calendar

YEARS_THRESHOLD = 365
LEAP_YEAR_THRESHOLD = 366

def compute_precise_years(start_date: date, end_date: date) -> int:
    total_days = (end_date - start_date).days
    if total_days < 0:
        raise ValueError("start_date must be before end_date")
    
    if total_days < YEARS_THRESHOLD:
        return 0
    
    year_count = 0
    current_date = start_date
    
    while True:
        next_year_date = date(current_date.year + 1, current_date.month, current_date.day)
        days_in_year = (next_year_date - current_date).days
        
        if total_days >= days_in_year:
            total_days -= days_in_year
            year_count += 1
            current_date = next_year_date
        else:
            break
            
    return year_count

if __name__ == '__main__':
    start = date(2000, 2, 29)
    end = date(2024, 3, 1)
    result = compute_precise_years(start, end)
    print(result)