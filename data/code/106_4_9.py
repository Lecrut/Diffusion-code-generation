from datetime import date
from calendar import isleap

def compute_absolute_year_gap(d1: date, d2: date) -> int:
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise ValueError("Inputs must be date objects")
    
    delta = d2 - d1
    days = abs(delta.days)
    
    if days < 0:
        raise ValueError("Invalid date difference")
    
    if days == 0:
        return 0
    
    year_diff = abs(d2.year - d1.year)
    
    if days >= 366 * year_diff:
        return year_diff
    
    start_year = min(d1.year, d2.year)
    end_year = max(d1.year, d2.year)
    
    total_days_in_range = 0
    for y in range(start_year, end_year):
        if isleap(y):
            total_days_in_range += 366
        else:
            total_days_in_range += 365
    
    if days >= total_days_in_range:
        return year_diff
    
    return year_diff - 1

if __name__ == '__main__':
    d1 = date(2020, 1, 1)
    d2 = date(2025, 1, 1)
    result = compute_absolute_year_gap(d1, d2)
    print(result)
    
    d3 = date(2023, 10, 15)
    d4 = date(2020, 10, 15)
    result2 = compute_absolute_year_gap(d3, d4)
    print(result2)
    
    d5 = date(2020, 3, 1)
    d6 = date(2021, 2, 28)
    result3 = compute_absolute_year_gap(d5, d6)
    print(result3)