def format_duration(duration_str):
    if not duration_str or not isinstance(duration_str, str):
        return "Invalid input"
    
    parts = duration_str.split(':')
    if len(parts) != 3:
        return "Invalid input"
    
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
    except ValueError:
        return "Invalid input"
    
    if hours < 0 or minutes < 0 or seconds < 0:
        return "Invalid input"
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    
    hours_rem = remaining // 3600
    remaining %= 3600
    
    minutes_rem = remaining // 60
    seconds_rem = remaining % 60
    
    result_parts = []
    
    if days > 0:
        result_parts.append(f"{days} Day" if days == 1 else f"{days} Days")
    
    if hours_rem > 0:
        result_parts.append(f"{hours_rem} Hour" if hours_rem == 1 else f"{hours_rem} Hours")
    
    if minutes_rem > 0:
        result_parts.append(f"{minutes_rem} Minute" if minutes_rem == 1 else f"{minutes_rem} Minutes")
    
    if seconds_rem > 0:
        result_parts.append(f"{seconds_rem} Second" if seconds_rem == 1 else f"{seconds_rem} Seconds")
    
    if not result_parts:
        return "0 Seconds"
    
    if len(result_parts) == 1:
        return result_parts[0]
    
    if len(result_parts) == 2:
        return " and ".join(result_parts)
    
    return ", ".join(result_parts[:-1]) + " and " + result_parts[-1]

if __name__ == '__main__':
    sample_input = "1:05:30"
    print(format_duration(sample_input))
    sample_input_2 = "24:00:00"
    print(format_duration(sample_input_2))
    sample_input_3 = "0:00:05"
    print(format_duration(sample_input_3))
    sample_input_4 = "10:00:00"
    print(format_duration(sample_input_4))