def time_string_to_human_readable(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in 'HH:MM:SS' format")
    
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    
    hours_from_remaining = remaining_seconds // 3600
    remaining_seconds %= 3600
    
    minutes_from_remaining = remaining_seconds // 60
    seconds_from_remaining = remaining_seconds % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours_from_remaining > 0:
        parts.append(f"{hours_from_remaining} hour{'s' if hours_from_remaining != 1 else ''}")
    if minutes_from_remaining > 0:
        parts.append(f"{minutes_from_remaining} minute{'s' if minutes_from_remaining != 1 else ''}")
    if seconds_from_remaining > 0 or (not parts):
        parts.append(f"{seconds_from_remaining} second{'s' if seconds_from_remaining != 1 else ''}")
    
    return ", ".join(parts)

if __name__ == '__main__':
    sample_time = "25:10:45"
    result = time_string_to_human_readable(sample_time)
    print(result)
    
    sample_time_2 = "00:00:05"
    result_2 = time_string_to_human_readable(sample_time_2)
    print(result_2)
    
    sample_time_3 = "48:00:00"
    result_3 = time_string_to_human_readable(sample_time_3)
    print(result_3)