from datetime import datetime

def calculate_time_left_in_month(start_date_str: str, end_date_str: str) -> dict:
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")
    
    total_seconds = int((end_date - start_date).total_seconds())
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "total_seconds": total_seconds
    }

if __name__ == '__main__':
    result = calculate_time_left_in_month("2023-10-01", "2023-10-31")
    print(result)