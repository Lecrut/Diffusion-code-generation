from datetime import datetime, timedelta

def calculate_time_left_in_month(start_date: datetime, end_date: datetime) -> dict:
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")
    
    if start_date.year != end_date.year or start_date.month != end_date.month:
        raise ValueError("Start and end dates must be in the same month")
    
    days_left = (end_date - start_date).days
    hours_left = days_left * 24
    minutes_left = hours_left * 60
    seconds_left = minutes_left * 60
    
    return {
        "days": days_left,
        "hours": hours_left,
        "minutes": minutes_left,
        "seconds": seconds_left
    }

if __name__ == '__main__':
    start = datetime(2023, 10, 1, 0, 0, 0)
    end = datetime(2023, 10, 31, 23, 59, 59)
    result = calculate_time_left_in_month(start, end)
    print(result)