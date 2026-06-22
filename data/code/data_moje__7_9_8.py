import datetime

def calculate_time_difference(start_time, end_time, unit):
    if start_time > end_time:
        raise ValueError("Start time must be before end time")
    
    delta = end_time - start_time
    total_seconds = delta.total_seconds()
    
    if unit == 'days':
        return total_seconds / 86400
    elif unit == 'hours':
        return total_seconds / 3600
    elif unit == 'minutes':
        return total_seconds / 60
    elif unit == 'seconds':
        return total_seconds
    elif unit == 'milliseconds':
        return total_seconds * 1000
    else:
        raise ValueError(f"Unsupported unit: {unit}")

def format_time_difference(start_time, end_time):
    if start_time > end_time:
        raise ValueError("Start time must be before end time")
    
    delta = end_time - start_time
    total_seconds = int(delta.total_seconds())
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return days, hours, minutes, seconds

if __name__ == '__main__':
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 3, 14, 30, 45)
    
    result_days = calculate_time_difference(start, end, 'days')
    result_hours = calculate_time_difference(start, end, 'hours')
    result_minutes = calculate_time_difference(start, end, 'minutes')
    
    formatted = format_time_difference(start, end)
    
    print(result_days)
    print(result_hours)
    print(result_minutes)
    print(f"Days: {formatted[0]}, Hours: {formatted[1]}, Minutes: {formatted[2]}, Seconds: {formatted[3]}")