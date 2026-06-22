def time_string_to_seconds(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_human_readable(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative")
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    seconds = remaining % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} day" + ("s" if days != 1 else ""))
    if hours > 0:
        parts.append(f"{hours} hour" + ("s" if hours != 1 else ""))
    if minutes > 0:
        parts.append(f"{minutes} minute" + ("s" if minutes != 1 else ""))
    if seconds > 0 or not parts:
        parts.append(f"{seconds} second" + ("s" if seconds != 1 else ""))
    
    return ", ".join(parts)

def convert_time(time_str):
    total_seconds = time_string_to_seconds(time_str)
    return seconds_to_human_readable(total_seconds)

if __name__ == '__main__':
    sample_time = "01:02:03"
    result = convert_time(sample_time)
    print(result)
    
    sample_time_2 = "25:30:45"
    result_2 = convert_time(sample_time_2)
    print(result_2)
    
    sample_time_3 = "00:00:05"
    result_3 = convert_time(sample_time_3)
    print(result_3)