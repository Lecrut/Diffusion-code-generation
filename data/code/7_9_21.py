from datetime import datetime

def calculate_time_difference(start_datetime, end_datetime, unit):
    time_difference = end_datetime - start_datetime
    
    if unit == 'days':
        return time_difference.days
    elif unit == 'hours':
        total_seconds = time_difference.total_seconds()
        return total_seconds // 3600
    elif unit == 'minutes':
        total_seconds = time_difference.total_seconds()
        return (total_seconds % 3600) // 60
    else:
        raise ValueError("Unsupported unit. Please choose from 'days', 'hours', or 'minutes'.")

if __name__ == '__main__':
    start_time = datetime(2023, 1, 1, 12, 0)
    end_time = datetime(2023, 1, 2, 14, 30)
    
    days_difference = calculate_time_difference(start_time, end_time, 'days')
    hours_difference = calculate_time_difference(start_time, end_time, 'hours')
    minutes_difference = calculate_time_difference(start_time, end_time, 'minutes')
    
    print(f"Days difference: {days_difference}")
    print(f"Hours difference: {hours_difference}")
    print(f"Minutes difference: {minutes_difference}")