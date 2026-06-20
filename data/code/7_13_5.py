def time_to_seconds(time_str):
    parts = time_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_human(total_seconds):
    if total_seconds < 0:
        raise ValueError("Time duration cannot be negative")
    
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    secs = remaining % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} days")
    if hours > 0:
        parts.append(f"{hours} hours")
    if minutes > 0:
        parts.append(f"{minutes} minutes")
    if secs > 0 or not parts:
        parts.append(f"{secs} seconds")
    
    return ", ".join(parts)

if __name__ == '__main__':
    time_string = "25:00:01"
    total_sec = time_to_seconds(time_string)
    human_str = seconds_to_human(total_sec)
    print(f"{time_string} -> {total_sec} seconds -> {human_str}")