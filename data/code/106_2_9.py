from datetime import datetime

def get_year_delta(d1: datetime, d2: datetime) -> int:
    if d2 < d1:
        raise ValueError("d2 must be after d1")
    
    delta = d2.year - d1.year
    
    if delta == 0:
        return 0
    
    if d2.month < d1.month:
        return delta - 1
    
    if d2.month == d1.month and d2.day < d1.day:
        return delta - 1
    
    return delta

if __name__ == '__main__':
    a = datetime(2010, 3, 15)
    b = datetime(2023, 3, 14)
    val = get_year_delta(a, b)
    print(val)