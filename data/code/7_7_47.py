from datetime import datetime

def calculate_time_difference(start_datetime, end_datetime, unit):
    if not isinstance(start_datetime, datetime) or not isinstance(end_datetime, datetime):
        raise ValueError("Both start_datetime and end_datetime must be datetime objects.")
    if start_datetime > end_datetime:
        raise ValueError("start_datetime must be earlier than end_datetime.")
    
    time_difference = end_datetime - start_datetime
    total_seconds = int(time_difference.total_seconds())
    
    if unit == 'days':
        return time_difference.days
    elif unit == 'hours':
        hours = total_seconds // 3600
        remaining_minutes = (total_seconds % 3600) // 60
        return f"{hours} hours and {remaining_minutes} minutes"
    elif unit == 'minutes':
        minutes = total_seconds // 60
        remaining_seconds = total_seconds % 60
        return f"{minutes} minutes and {remaining_seconds} seconds"
    else:
        raise ValueError("Unsupported unit. Use 'days', 'hours', or 'minutes'.")

if __name__ == '__main__':
    start_datetime = datetime(2023, 1, 1, 12, 0, 0)
    end_datetime = datetime(2023, 1, 2, 14, 30, 0)
    
    days_difference = calculate_time_difference(start_datetime, end_datetime, 'days')
    hours_difference = calculate_time_difference(start_datetime, end_datetime, 'hours')
    minutes_difference = calculate_time_difference(start_datetime, end_datetime, 'minutes')
    
    print(f"Days difference: {days_difference}")
    print(f"Hours and minutes difference: {hours_difference}")
    print(f"Minutes and seconds difference: {minutes_difference}")