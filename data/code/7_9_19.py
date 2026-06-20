import datetime
import math

def calculate_time_difference(start_time, end_time, unit):
    if start_time > end_time:
        start_time, end_time = end_time, start_time
    
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
    else:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: days, hours, minutes, seconds.")

def get_detailed_difference(start_time, end_time):
    if start_time > end_time:
        start_time, end_time = end_time, start_time
    
    delta = end_time - start_time
    total_seconds = delta.total_seconds()
    
    days = int(total_seconds // 86400)
    remaining_seconds = total_seconds % 86400
    
    hours = int(remaining_seconds // 3600)
    remaining_seconds = remaining_seconds % 3600
    
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)
    
    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

def format_detailed_difference(diff_dict):
    parts = []
    if diff_dict['days'] > 0:
        parts.append(f"{diff_dict['days']} day{'s' if diff_dict['days'] != 1 else ''}")
    if diff_dict['hours'] > 0:
        parts.append(f"{diff_dict['hours']} hour{'s' if diff_dict['hours'] != 1 else ''}")
    if diff_dict['minutes'] > 0:
        parts.append(f"{diff_dict['minutes']} minute{'s' if diff_dict['minutes'] != 1 else ''}")
    if diff_dict['seconds'] > 0 or not parts:
        parts.append(f"{diff_dict['seconds']} second{'s' if diff_dict['seconds'] != 1 else ''}")
    
    return ", ".join(parts)

if __name__ == '__main__':
    start_dt = datetime.datetime(2023, 6, 15, 10, 30, 0)
    end_dt = datetime.datetime(2023, 6, 17, 14, 45, 30)
    
    total_hours = calculate_time_difference(start_dt, end_dt, 'hours')
    print(f"Total hours difference: {total_hours}")
    
    detailed = get_detailed_difference(start_dt, end_dt)
    formatted_output = format_detailed_difference(detailed)
    print(f"Detailed difference: {formatted_output}")