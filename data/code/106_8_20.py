from datetime import datetime

YEARS_MAPPING = {
    1: 365,
    4: 1461,
    10: 3652,
    20: 7305,
    100: 36525,
}

def compute_year_delta(start: datetime, end: datetime) -> int:
    if start.year > end.year:
        start, end = end, start
    
    total_days = (end - start).days
    
    if total_days < 0:
        return 0
    
    count = 0
    remaining = total_days
    
    for years_key in sorted(YEARS_MAPPING.keys(), reverse=True):
        days_in_period = YEARS_MAPPING[years_key]
        if remaining >= days_in_period:
            count += years_key
            remaining -= days_in_period
            
    if remaining > 0:
        current_year = start.year + count
        days_in_current = 366 if (current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)) else 365
        if remaining >= days_in_current:
            count += 1
            
    return count

if __name__ == '__main__':
    t1 = datetime(2020, 2, 29)
    t2 = datetime(2024, 2, 28)
    ans = compute_year_delta(t1, t2)
    print(ans)