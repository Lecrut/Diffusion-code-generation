from datetime import datetime, timedelta

def calculate_time_left_in_month(start_date: datetime, end_date: datetime) -> dict:
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")
    
    if start_date.month == end_date.month and start_date.year == end_date.year:
        total_seconds = int((end_date - start_date).total_seconds())
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": total_seconds
        }
    
    days_in_month = (end_date.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    days_in_month = days_in_month.day
    
    days_passed = start_date.day - 1
    remaining_days = days_in_month - days_passed
    
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minute = 60
    
    total_remaining_seconds = remaining_days * 86400
    days = total_remaining_seconds // 86400
    hours = (total_remaining_seconds % 86400) // 3600
    minutes = (total_remaining_seconds % 3600) // 60
    seconds = total_remaining_seconds % 60
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "total_seconds": total_remaining_seconds
    }

if __name__ == '__main__':
    start = datetime(2023, 10, 15, 10, 30, 0)
    end = datetime(2023, 10, 31, 23, 59, 59)
    result = calculate_time_left_in_month(start, end)
    print(result)