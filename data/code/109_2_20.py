from datetime import datetime, timedelta

def calculate_remaining_month_time(year: int, month: int, day: int, hour: int, minute: int, second: int) -> timedelta:
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    if not (1 <= day <= 31):
        raise ValueError(f"Invalid day: {day}")
    if not (0 <= hour <= 23):
        raise ValueError(f"Invalid hour: {hour}")
    if not (0 <= minute <= 59):
        raise ValueError(f"Invalid minute: {minute}")
    if not (0 <= second <= 59):
        raise ValueError(f"Invalid second: {second}")

    current_date = datetime(year, month, day, hour, minute, second)
    start_of_month = datetime(year, month, 1, 0, 0, 0)
    
    if month == 12:
        next_month_start = datetime(year + 1, 1, 1, 0, 0, 0)
    else:
        next_month_start = datetime(year, month + 1, 1, 0, 0, 0)
    
    end_of_month = next_month_start - timedelta(seconds=1)
    
    if current_date < start_of_month:
        return end_of_month - start_of_month
    elif current_date > end_of_month:
        return timedelta(0)
    else:
        return end_of_month - current_date

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    sample_hour = 12
    sample_minute = 0
    sample_second = 0
    
    result = calculate_remaining_month_time(sample_year, sample_month, sample_day, sample_hour, sample_minute, sample_second)
    print(result)