from datetime import datetime, timedelta

def calculate_time_left_in_month(start_date_str: str, end_date_str: str) -> dict:
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")
    
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
    result = calculate_time_left_in_month("2023-10-01", "2023-10-31")
    print(result)