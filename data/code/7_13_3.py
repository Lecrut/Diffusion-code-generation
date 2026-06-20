def parse_time_to_seconds(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_readable(total_seconds):
    if total_seconds < 0:
        total_seconds = 0
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    secs = remaining % 60

    parts = []
    if days > 0:
        unit = "day" if days == 1 else "days"
        parts.append(f"{days} {unit}")
    if hours > 0:
        unit = "hour" if hours == 1 else "hours"
        parts.append(f"{hours} {unit}")
    if minutes > 0:
        unit = "minute" if minutes == 1 else "minutes"
        parts.append(f"{minutes} {unit}")
    if secs > 0:
        unit = "second" if secs == 1 else "seconds"
        parts.append(f"{secs} {unit}")
    
    if not parts:
        return "0 seconds"
    
    return ", ".join(parts)

if __name__ == '__main__':
    raw_time = "90:61:10"
    total_secs = parse_time_to_seconds(raw_time)
    readable = seconds_to_readable(total_secs)
    print(readable)