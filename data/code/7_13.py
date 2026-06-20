def convert_time_to_readable(time_string):
    parts = time_string.split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in HH:MM:SS format")
    
    hours, minutes, seconds = map(int, parts)
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours_from_remaining = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes_from_remaining = remaining_seconds // 60
    seconds_from_remaining = remaining_seconds % 60
    
    parts_result = []
    if days > 0:
        parts_result.append(f"{days} days")
    if hours_from_remaining > 0:
        parts_result.append(f"{hours_from_remaining} hours")
    if minutes_from_remaining > 0:
        parts_result.append(f"{minutes_from_remaining} minutes")
    if seconds_from_remaining > 0 or not parts_result:
        parts_result.append(f"{seconds_from_remaining} seconds")
    
    return ', '.join(parts_result)

if __name__ == '__main__':
    sample_times = ['00:00:00', '12:30:45', '25:00:00', '01:02:03', '48:00:00']
    for time_str in sample_times:
        result = convert_time_to_readable(time_str)
        print(result)