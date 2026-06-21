from datetime import datetime, timedelta

def calculate_time_left_in_month(start_date: str, end_date: str) -> dict:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    if start > end:
        raise ValueError("Start date must be before or equal to end date")
    
    total_seconds = int((end - start).total_seconds())
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {
        "total_days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "formatted": f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    }

if __name__ == '__main__':
    start_date = "2023-10-01"
    end_date = "2023-10-31"
    
    result = calculate_time_left_in_month(start_date, end_date)
    print(result["formatted"])