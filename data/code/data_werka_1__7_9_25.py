from datetime import datetime

def calculate_time_difference(datetime1, datetime2, unit):
    difference = abs((datetime2 - datetime1).total_seconds())
    
    if unit == 'days':
        return round(difference / 86400)
    elif unit == 'hours':
        return round(difference / 3600)
    elif unit == 'minutes':
        return round(difference / 60)
    else:
        raise ValueError("Unsupported unit. Please choose from 'days', 'hours', or 'minutes'.")

if __name__ == '__main__':
    # Sample datetime objects
    dt1 = datetime(2023, 10, 1, 12, 0)
    dt2 = datetime(2023, 10, 5, 14, 30)
    
    # Calculate difference in days
    days_difference = calculate_time_difference(dt1, dt2, 'days')
    print(f"Days difference: {days_difference}")
    
    # Calculate difference in hours
    hours_difference = calculate_time_difference(dt1, dt2, 'hours')
    print(f"Hours difference: {hours_difference}")
    
    # Calculate difference in minutes
    minutes_difference = calculate_time_difference(dt1, dt2, 'minutes')
    print(f"Minutes difference: {minutes_difference}")