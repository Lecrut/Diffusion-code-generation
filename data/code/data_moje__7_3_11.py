def format_duration(duration_string):
    if not isinstance(duration_string, str) or len(duration_string.split(':')) != 3:
        raise ValueError("Invalid format. Expected 'HH:MM:SS'")
    
    try:
        hours_str, minutes_str, seconds_str = duration_string.split(':')
        total_seconds = int(hours_str) * 3600 + int(minutes_str) * 60 + int(seconds_str)
    except ValueError:
        raise ValueError("Time components must be integers")
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} Days" if days == 1 else f"{days} Days")
    if hours > 0:
        parts.append(f"{hours} Hour" if hours == 1 else f"{hours} Hours")
    if minutes > 0:
        parts.append(f"{minutes} Minute" if minutes == 1 else f"{minutes} Minutes")
    if seconds > 0:
        parts.append(f"{seconds} Second" if seconds == 1 else f"{seconds} Seconds")
    
    if not parts:
        return "0 Seconds"
    
    return ", ".join(parts)

if __name__ == '__main__':
    test_cases = ["00:00:00", "01:00:00", "24:00:00", "25:01:01", "00:00:30", "100:00:00"]
    for case in test_cases:
        result = format_duration(case)
        print(f"{case} -> {result}")