def time_to_seconds(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return hours * 3600 + minutes * 60 + seconds

def format_duration(total_seconds):
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    secs = remainder % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} day") if days == 1 else parts.append(f"{days} days")
    if hours > 0:
        parts.append(f"{hours} hour") if hours == 1 else parts.append(f"{hours} hours")
    if minutes > 0:
        parts.append(f"{minutes} minute") if minutes == 1 else parts.append(f"{minutes} minutes")
    if secs > 0 or not parts:
        parts.append(f"{secs} second") if secs == 1 else parts.append(f"{secs} seconds")
        
    return ", ".join(parts)

def convert_time(time_str):
    total_secs = time_to_seconds(time_str)
    return format_duration(total_secs)

if __name__ == '__main__':
    sample_time = "25:61:61"
    result = convert_time(sample_time)
    print(result)