def time_to_seconds(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_human_readable(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative")
    
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    secs = remaining % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if secs > 0 or not parts:
        parts.append(f"{secs} second{'s' if secs != 1 else ''}")
    
    return ', '.join(parts)

if __name__ == '__main__':
    time_input = "25:61:61"
    total_secs = time_to_seconds(time_input)
    human_readable = seconds_to_human_readable(total_secs)
    print(human_readable)