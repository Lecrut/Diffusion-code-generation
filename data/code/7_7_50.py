from datetime import datetime

def calculate_time_difference(start_datetime, end_datetime, unit):
    if start_datetime > end_datetime:
        raise ValueError("Start datetime must be before end datetime")
    
    time_difference = end_datetime - start_datetime
    
    if unit == 'days':
        return time_difference.days
    elif unit == 'hours':
        return int(time_difference.total_seconds() / 3600)
    elif unit == 'minutes':
        return int(time_difference.total_seconds() / 60)
    else:
        raise ValueError("Unsupported unit. Please choose from 'days', 'hours', or 'minutes'.")

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 12, 0, 0)
    end = datetime(2023, 1, 2, 14, 30, 0)
    
    days_difference = calculate_time_difference(start, end, 'days')
    hours_difference = calculate_time_difference(start, end, 'hours')
    minutes_difference = calculate_time_difference(start, end, 'minutes')
    
    print(f"Days difference: {days_difference}")
    print(f"Hours difference: {hours_difference}")
    print(f"Minutes difference: {minutes_difference}")