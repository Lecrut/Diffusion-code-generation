from datetime import date

def get_absolute_year_diff(d1: date, d2: date) -> int:
    if not isinstance(d1, date) or not isinstance(d2, date):
        raise ValueError("Inputs must be date objects")
    
    if d1 == d2:
        return 0
    
    earlier = d1 if d1 < d2 else d2
    later = d2 if d1 < d2 else d1
    
    year_diff = later.year - earlier.year
    
    if later.month < earlier.month:
        return year_diff - 1
    if later.month == earlier.month and later.day < earlier.day:
        return year_diff - 1
    
    return year_diff

if __name__ == '__main__':
    start = date(2020, 1, 1)
    end = date(2025, 1, 1)
    diff = get_absolute_year_diff(start, end)
    print(diff)