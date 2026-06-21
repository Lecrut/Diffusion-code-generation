from datetime import datetime, timedelta

def calculate_remaining_time(year: int, month: int, day: int, hour: int, minute: int, second: int) -> timedelta:
    current_time = datetime(year, month, day, hour, minute, second)
    start_of_month = datetime(year, month, 1)
    
    if month == 12:
        end_of_month = datetime(year + 1, 1, 1) - timedelta(seconds=1)
    else:
        end_of_month = datetime(year, month + 1, 1) - timedelta(seconds=1)
    
    if current_time < start_of_month:
        remaining = end_of_month - start_of_month
    elif current_time > end_of_month:
        remaining = timedelta(0)
    else:
        remaining = end_of_month - current_time
        
    return remaining

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 15
    sample_hour = 14
    sample_minute = 30
    sample_second = 0
    
    result = calculate_remaining_time(sample_year, sample_month, sample_day, sample_hour, sample_minute, sample_second)
    print(result)