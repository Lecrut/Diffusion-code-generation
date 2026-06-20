def convert_time_string(time_string):
    parts = time_string.split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in 'HH:MM:SS' format")
    
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
    except ValueError:
        raise ValueError("Time components must be integers")
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    
    readable_parts = []
    if days > 0:
        readable_parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        readable_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        readable_parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0 or not readable_parts:
        readable_parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    return ', '.join(readable_parts)

if __name__ == '__main__':
    sample_times = [
        "00:00:00",
        "01:02:03",
        "23:59:59",
        "25:00:00",
        "48:30:15",
        "00:00:01",
        "12:30:45",
        "99:99:99"
    ]
    
    for time_str in sample_times:
        result = convert_time_string(time_str)
        print(f"{time_str} -> {result}")