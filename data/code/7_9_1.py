import datetime

def calculate_time_difference(start_time, end_time, unit):
    if start_time > end_time:
        start_time, end_time = end_time, start_time
    
    delta = end_time - start_time
    total_seconds = int(delta.total_seconds())
    
    if unit == 'days':
        return total_seconds / 86400
    elif unit == 'hours':
        return total_seconds / 3600
    elif unit == 'minutes':
        return total_seconds / 60
    elif unit == 'seconds':
        return total_seconds
    elif unit == 'structured':
        days = total_seconds // 86400
        remaining_seconds = total_seconds % 86400
        hours = remaining_seconds // 3600
        remaining_seconds = remaining_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    start = datetime.datetime(2023, 1, 1, 10, 30, 0)
    end = datetime.datetime(2023, 1, 3, 14, 45, 30)
    
    days_diff = calculate_time_difference(start, end, 'days')
    hours_diff = calculate_time_difference(start, end, 'hours')
    structured_diff = calculate_time_difference(start, end, 'structured')
    
    print(days_diff)
    print(hours_diff)
    print(structured_diff)