from datetime import date
from calendar import isleap

YEARS_OFFSET = date.today()

def compute_full_years(first: date, second: date) -> int:
    if first > second:
        raise ValueError("first must precede second")
    if first == second:
        return 0
    
    target_year = first.year
    days_in_target = 366 if isleap(target_year) else 365
    
    current = first
    count = 0
    
    while True:
        next_anniversary = date(target_year + 1, first.month, first.day)
        if next_anniversary > second:
            break
        
        current = next_anniversary
        count += 1
        target_year += 1
        
        if current.month == 2 and current.day == 29:
            days_in_target = 366 if isleap(target_year) else 365
            
    return count

if __name__ == '__main__':
    start = date(2000, 2, 28)
    finish = date(2024, 3, 1)
    years = compute_full_years(start, finish)
    print(years)