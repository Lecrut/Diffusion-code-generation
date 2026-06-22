import datetime

def calculate_time_difference(start_time, end_time, unit):
    if start_time > end_time:
        raise ValueError("Start time must be before or equal to end time")
    
    delta = end_time - start_time
    total_seconds = int(delta.total_seconds())
    
    if unit == 'days':
        return total_seconds // 86400
    elif unit == 'hours':
        return total_seconds // 3600
    elif unit == 'minutes':
        return total_seconds // 60
    elif unit == 'seconds':
        return total_seconds
    elif unit == 'hours_and_minutes':
        hours = total_seconds // 3600
        remaining_minutes = (total_seconds % 3600) // 60
        return f"{hours} hours and {remaining_minutes} minutes"
    elif unit == 'days_and_hours':
        days = total_seconds // 86400
        remaining_hours = (total_seconds % 86400) // 3600
        return f"{days} days and {remaining_hours} hours"
    elif unit == 'days_hours_minutes':
        days = total_seconds // 86400
        remaining_seconds_after_days = total_seconds % 86400
        hours = remaining_seconds_after_days // 3600
        remaining_minutes = (remaining_seconds_after_days % 3600) // 60
        return f"{days} days, {hours} hours, and {remaining_minutes} minutes"
    else:
        raise ValueError("Unsupported unit. Choose from 'days', 'hours', 'minutes', 'seconds', 'hours_and_minutes', 'days_and_hours', or 'days_hours_minutes'")

if __name__ == '__main__':
    start_dt = datetime.datetime(2023, 10, 1, 8, 30, 0)
    end_dt = datetime.datetime(2023, 10, 3, 14, 45, 30)
    
    result_days = calculate_time_difference(start_dt, end_dt, 'days')
    print(result_days)
    
    result_hours = calculate_time_difference(start_dt, end_dt, 'hours')
    print(result_hours)
    
    result_minutes = calculate_time_difference(start_dt, end_dt, 'minutes')
    print(result_minutes)
    
    result_hm = calculate_time_difference(start_dt, end_dt, 'hours_and_minutes')
    print(result_hm)
    
    result_dhm = calculate_time_difference(start_dt, end_dt, 'days_hours_minutes')
    print(result_dhm)