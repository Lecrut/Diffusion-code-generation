def time_string_to_human_readable(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Input must be in 'HH:MM:SS' format")
    
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
    except ValueError:
        raise ValueError("Hours, minutes, and seconds must be integers")
    
    if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
        raise ValueError("Invalid time values")
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days, remainder = divmod(total_seconds, 86400)
    hours_rem, remainder = divmod(remainder, 3600)
    minutes_rem, seconds_rem = divmod(remainder, 60)
    
    result_parts = []
    if days > 0:
        result_parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours_rem > 0:
        result_parts.append(f"{hours_rem} hour{'s' if hours_rem != 1 else ''}")
    if minutes_rem > 0:
        result_parts.append(f"{minutes_rem} minute{'s' if minutes_rem != 1 else ''}")
    if seconds_rem > 0 or not result_parts:
        result_parts.append(f"{seconds_rem} second{'s' if seconds_rem != 1 else ''}")
    
    return ", ".join(result_parts)

if __name__ == '__main__':
    sample_inputs = ["00:00:00", "01:02:03", "25:00:00", "1:30:45", "02:00:00"]
    for s in sample_inputs:
        print(time_string_to_human_readable(s))