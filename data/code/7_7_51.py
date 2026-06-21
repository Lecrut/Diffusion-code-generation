from datetime import datetime, timedelta

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
        return total_seconds // 3600
    elif unit == 'minutes':
        return (total_seconds % 3600) // 60
    else:
        raise ValueError("Unsupported unit. Use 'days', 'hours', or 'minutes'.")

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 12, 0)
    end = datetime(2023, 1, 2, 14, 30)

    days_difference = calculate_time_difference(start, end, 'days')
    hours_difference = calculate_time_difference(start, end, 'hours')
    minutes_difference = calculate_time_difference(start, end, 'minutes')

    print(f"Days: {days_difference}")
    print(f"Hours: {hours_difference}")
    print(f"Minutes: {minutes_difference}")