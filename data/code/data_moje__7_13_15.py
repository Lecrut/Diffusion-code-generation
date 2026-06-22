def parse_time_string(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in HH:MM:SS format")
    
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
        raise ValueError("Invalid time values")
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def total_seconds_to_human_readable(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative")
    
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    
    hours = remaining // 3600
    remaining = remaining % 3600
    
    minutes = remaining // 60
    seconds = remaining % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} days")
    if hours > 0:
        parts.append(f"{hours} hours")
    if minutes > 0:
        parts.append(f"{minutes} minutes")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} seconds")
    
    return ", ".join(parts)

def convert_time_to_human_readable(time_str):
    total_seconds = parse_time_string(time_str)
    return total_seconds_to_human_readable(total_seconds)

if __name__ == '__main__':
    sample_times = ["00:00:00", "01:30:45", "24:00:00", "30:15:30"]
    for t in sample_times:
        try:
            result = convert_time_to_human_readable(t)
            print(f"{t} -> {result}")
        except ValueError as e:
            print(f"{t} -> Error: {e}")