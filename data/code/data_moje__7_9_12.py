from datetime import datetime

def calculate_time_difference(start_dt, end_dt, unit):
    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())
    
    if total_seconds < 0:
        raise ValueError("End time must be after start time")
    
    if unit == 'days':
        days = total_seconds // 86400
        remaining_seconds = total_seconds % 86400
        hours = remaining_seconds // 3600
        remaining_seconds = remaining_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds"
    
    elif unit == 'hours':
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours} hours, {minutes} minutes, and {seconds} seconds"
    
    elif unit == 'minutes':
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes} minutes and {seconds} seconds"
    
    elif unit == 'seconds':
        return f"{total_seconds} seconds"
    
    else:
        raise ValueError(f"Unsupported unit: {unit}. Use 'days', 'hours', 'minutes', or 'seconds'.")

if __name__ == '__main__':
    start_time = datetime(2023, 6, 15, 10, 30, 0)
    end_time = datetime(2023, 6, 17, 14, 45, 30)
    result = calculate_time_difference(start_time, end_time, 'days')
    print(result)