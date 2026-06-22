from datetime import datetime, timedelta

def calculate_time_left_in_month(start_date: datetime, end_date: datetime) -> dict:
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")
    
    if start_date.month == end_date.month and start_date.year == end_date.year:
        days_left = (end_date - start_date).days
        hours_left = (end_date - start_date).total_seconds() / 3600
        minutes_left = (end_date - start_date).total_seconds() / 60
        seconds_left = (end_date - start_date).total_seconds()
        
        return {
            "days": days_left,
            "hours": hours_left,
            "minutes": minutes_left,
            "seconds": seconds_left
        }
    
    days_in_month = (end_date.replace(day=1) + timedelta(days=32)).day
    days_in_month = days_in_month - end_date.day
    
    remaining_days = days_in_month
    remaining_hours = remaining_days * 24
    remaining_minutes = remaining_hours * 60
    remaining_seconds = remaining_minutes * 60
    
    return {
        "days": remaining_days,
        "hours": remaining_hours,
        "minutes": remaining_minutes,
        "seconds": remaining_seconds
    }

if __name__ == '__main__':
    start = datetime(2023, 10, 15, 10, 30, 0)
    end = datetime(2023, 10, 31, 23, 59, 59)
    
    result = calculate_time_left_in_month(start, end)
    print(result)