from datetime import datetime, timedelta

def fraction_of_month_remaining(year: int, month: int) -> float:
    start = datetime(year, month, 1)
    if month == 12:
        end = datetime(year + 1, 1, 1)
    else:
        end = datetime(year, month + 1, 1)
    
    total_seconds = (end - start).total_seconds()
    if total_seconds <= 0:
        return 0.0
    
    now = datetime.now()
    
    if now < start:
        return 1.0
    
    if now >= end:
        return 0.0
    
    elapsed = (now - start).total_seconds()
    
    remaining_fraction = 1.0 - (elapsed / total_seconds)
    
    if remaining_fraction < 0.0:
        return 0.0
    if remaining_fraction > 1.0:
        return 1.0
        
    return remaining_fraction

if __name__ == '__main__':
    current_year = datetime.now().year
    current_month = datetime.now().month
    result = fraction_of_month_remaining(current_year, current_month)
    print(result)