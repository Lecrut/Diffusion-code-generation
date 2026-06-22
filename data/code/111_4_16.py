from datetime import timedelta, date
from calendar import isleap

def get_seconds_in_non_leap_year():
    target_year = 2023
    if isleap(target_year):
        raise ValueError(f"{target_year} is a leap year, not a non-leap year.")
    
    start = date(target_year, 1, 1)
    end = date(target_year, 12, 31)
    
    delta = end - start
    days = delta.days
    
    if days != 364:
        raise ValueError(f"Expected 364 days between Jan 1 and Dec 31 inclusive of start, got {days}.")
    
    total_days_in_year = 365
    seconds_per_day = 86400
    
    return total_days_in_year * seconds_per_day

if __name__ == '__main__':
    result = get_seconds_in_non_leap_year()
    print(result)