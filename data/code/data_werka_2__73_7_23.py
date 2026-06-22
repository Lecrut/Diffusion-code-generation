from datetime import datetime
import calendar

def get_minutes_between(start_str: str, end_str: str) -> float:
    if not start_str or not end_str:
        raise ValueError("Dates cannot be empty")
    try:
        year, month, day = map(int, start_str.split('-'))
        hour, minute, second = map(int, start_str.split(' ')[1].split(':'))
        start_dt = datetime(year, month, day, hour, minute, second)
    except (ValueError, IndexError) as e:
        raise ValueError(f"Invalid start date format: {e}")
    
    try:
        year, month, day = map(int, end_str.split('-'))
        hour, minute, second = map(int, end_str.split(' ')[1].split(':'))
        end_dt = datetime(year, month, day, hour, minute, second)
    except (ValueError, IndexError) as e:
        raise ValueError(f"Invalid end date format: {e}")
    
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    return total_seconds / 60

if __name__ == '__main__':
    date_a = '2023-01-01 10:00:00'
    date_b = '2023-01-01 12:30:00'
    diff = get_minutes_between(date_a, date_b)
    print(diff)