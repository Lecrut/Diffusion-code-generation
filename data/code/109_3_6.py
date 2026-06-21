import calendar
from datetime import datetime, timedelta
from dataclasses import dataclass

_DAYS_IN_STANDARD_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

@dataclass
class MonthDuration:
    days_left: int
    is_leap_year: bool

def calculate_remaining_days(year: int, month: int, day: int) -> MonthDuration:
    if not 1 <= month <= 12:
        raise ValueError("Month out of range")
    if not 1 <= day <= 31:
        raise ValueError("Day out of range")
    
    is_leap = calendar.isleap(year)
    base_days = _DAYS_IN_STANDARD_MONTH[month - 1]
    total_days = 29 if (month == 2 and is_leap) else base_days
    
    if day > total_days:
        raise ValueError(f"Invalid day {day} for month {month} in year {year}")
    
    current = datetime(year, month, day)
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    
    delta = next_month - current
    remaining = delta.days
    
    return MonthDuration(days_left=remaining, is_leap_year=is_leap)

if __name__ == '__main__':
    result = calculate_remaining_days(2024, 2, 15)
    print(result.days_left)
    print(result.is_leap_year)