from datetime import datetime, timedelta

def calculate_time_left_in_month(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")
    
    days_left = (end_date - start_date).days
    hours_left = 23 - start_date.hour
    minutes_left = 59 - start_date.minute
    seconds_left = 59 - start_date.second
    
    total_seconds_left = (days_left * 24 * 3600) + (hours_left * 3600) + (minutes_left * 60) + seconds_left
    
    return {
        "days": days_left,
        "hours": hours_left,
        "minutes": minutes_left,
        "seconds": seconds_left,
        "total_seconds": total_seconds_left
    }

if __name__ == '__main__':
    start = "2023-10-15 14:30:45"
    end = "2023-10-31 23:59:59"
    result = calculate_time_left_in_month(start, end)
    print(result)