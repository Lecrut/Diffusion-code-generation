from datetime import datetime, timedelta
import calendar

def calculate_days_between(date1_str: str, date2_str: str) -> int:
    if not isinstance(date1_str, str) or not isinstance(date2_str, str):
        raise TypeError("Arguments must be strings")
    
    try:
        parts1 = date1_str.split('-')
        if len(parts1) != 3:
            raise ValueError("Date 1 must be in YYYY-MM-DD format")
        y1, m1, d1 = int(parts1[0]), int(parts1[1]), int(parts1[2])
        
        parts2 = date2_str.split('-')
        if len(parts2) != 3:
            raise ValueError("Date 2 must be in YYYY-MM-DD format")
        y2, m2, d2 = int(parts2[0]), int(parts2[1]), int(parts2[2])
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Date components must be integers") from e
        raise
    
    if m1 < 1 or m1 > 12 or d1 < 1 or d1 > 31:
        raise ValueError(f"Invalid month or day in date1: {date1_str}")
    if m2 < 1 or m2 > 12 or d2 < 1 or d2 > 31:
        raise ValueError(f"Invalid month or day in date2: {date2_str}")
        
    max_day1 = calendar.monthrange(y1, m1)[1]
    max_day2 = calendar.monthrange(y2, m2)[1]
    
    if d1 > max_day1:
        raise ValueError(f"Invalid day {d1} for month {m1} in {y1}")
    if d2 > max_day2:
        raise ValueError(f"Invalid day {d2} for month {m2} in {y2}")

    date1 = datetime(y1, m1, d1)
    date2 = datetime(y2, m2, d2)
    
    delta = date2 - date1
    return abs(delta.days)

if __name__ == '__main__':
    start = '2024-02-28'
    end = '2024-03-01'
    result = calculate_days_between(start, end)
    print(result)