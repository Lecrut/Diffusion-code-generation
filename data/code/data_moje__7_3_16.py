def convert_duration(duration_str):
    parts = duration_str.split(':')
    total_seconds = 0
    if len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
        total_seconds = hours * 3600 + minutes * 60 + seconds
    elif len(parts) == 2:
        hours, minutes = map(int, parts)
        total_seconds = hours * 3600 + minutes * 60
    elif len(parts) == 1:
        total_seconds = int(parts[0])
    
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    result_parts = []
    if days > 0:
        result_parts.append(f"{days} Day{'s' if days != 1 else ''}")
    if hours > 0:
        result_parts.append(f"{hours} Hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        result_parts.append(f"{minutes} Minute{'s' if minutes != 1 else ''}")
    if seconds > 0 or not result_parts:
        result_parts.append(f"{seconds} Second{'s' if seconds != 1 else ''}")
    
    return ", ".join(result_parts)

if __name__ == '__main__':
    sample1 = "10:05:30"
    sample2 = "01:30:00"
    sample3 = "00:00:05"
    sample4 = "25:00:00"
    sample5 = "86400:00:00"
    
    print(convert_duration(sample1))
    print(convert_duration(sample2))
    print(convert_duration(sample3))
    print(convert_duration(sample4))
    print(convert_duration(sample5))