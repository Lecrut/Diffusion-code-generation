from datetime import datetime

def calculate_time_difference(start_datetime, end_datetime, unit):
    # Calculate the difference in seconds
    difference = (end_datetime - start_datetime).total_seconds()
    
    if unit == 'days':
        return difference / 86400
    elif unit == 'hours':
        return difference / 3600
    elif unit == 'minutes':
        return difference / 60
    elif unit == 'seconds':
        return difference
    else:
        raise ValueError("Unsupported unit. Please choose from 'days', 'hours', 'minutes', or 'seconds'.")

if __name__ == '__main__':
    # Hard-coded sample values
    start_datetime = datetime(2023, 1, 1, 12, 0, 0)
    end_datetime = datetime(2023, 1, 2, 14, 30, 0)
    
    # Calculate time difference in days
    days_difference = calculate_time_difference(start_datetime, end_datetime, 'days')
    print(f"Time difference in days: {days_difference}")
    
    # Calculate time difference in hours
    hours_difference = calculate_time_difference(start_datetime, end_datetime, 'hours')
    print(f"Time difference in hours: {hours_difference}")
    
    # Calculate time difference in minutes
    minutes_difference = calculate_time_difference(start_datetime, end_datetime, 'minutes')
    print(f"Time difference in minutes: {minutes_difference}")
    
    # Calculate time difference in seconds
    seconds_difference = calculate_time_difference(start_datetime, end_datetime, 'seconds')
    print(f"Time difference in seconds: {seconds_difference}")