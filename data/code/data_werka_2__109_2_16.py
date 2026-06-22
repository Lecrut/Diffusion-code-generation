from datetime import datetime, timedelta

def calculate_remaining_month_time(year: int, month: int, day: int, hour: int, minute: int, second: int) -> timedelta:
    if month < 1 or month > 12:
        raise ValueError(f"Invalid month: {month}")
    
    start_date = datetime(year, month, 1)
    
    if month == 12:
        next_month_start = datetime(year + 1, 1, 1)
    else:
        next_month_start = datetime(year, month + 1, 1)
    
    end_date = next_month_start - timedelta(seconds=1)
    
    current_time = datetime(year, month, day, hour, minute, second)
    
    if current_time < start_date:
        return end_date - start_date
    
    if current_time > end_date:
        return timedelta(0)
    
    return end_date - current_time

if __name__ == '__main__':
    result = calculate_remaining_month_time(2023, 10, 15, 12, 0, 0)
    print(result)