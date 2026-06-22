from datetime import datetime, timedelta

def calculate_time_left_in_month(start_date: str, end_date: str) -> dict:
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    
    if start_dt > end_dt:
        raise ValueError("Start date must be before or equal to end date")
    
    if start_dt.month != end_dt.month:
        raise ValueError("Start and end dates must be in the same month")
    
    days_left = (end_dt - start_dt).days
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
    start = "2023-10-01"
    end = "2023-10-31"
    result = calculate_time_left_in_month(start, end)
    print(result)