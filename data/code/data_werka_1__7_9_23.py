from datetime import datetime

def calculate_time_difference(start_datetime, end_datetime, unit):
    # Calculate the difference in seconds
    time_difference = (end_datetime - start_datetime).total_seconds()
    
    if unit == 'days':
        return time_difference / 86400
    elif unit == 'hours':
        return time_difference / 3600
    elif unit == 'minutes':
        return time_difference / 60
    else:
        raise ValueError("Unsupported unit. Please choose from 'days', 'hours', or 'minutes'.")

if __name__ == '__main__':
    # Sample datetime objects
    start = datetime(2023, 1, 1, 12, 0)
    end = datetime(2023, 1, 2, 14, 30)
    
    # Calculate and print the time difference in days
    days_difference = calculate_time_difference(start, end, 'days')
    print(f"Time difference in days: {days_difference}")
    
    # Calculate and print the time difference in hours
    hours_difference = calculate_time_difference(start, end, 'hours')
    print(f"Time difference in hours: {hours_difference}")
    
    # Calculate and print the time difference in minutes
    minutes_difference = calculate_time_difference(start, end, 'minutes')
    print(f"Time difference in minutes: {minutes_difference}")