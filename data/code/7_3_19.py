def format_duration(duration_str):
    parts = duration_str.split(':')
    if len(parts) != 3:
        raise ValueError("Duration must be in HH:MM:SS format")
    
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
    except ValueError:
        raise ValueError("Duration components must be integers")
    
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Duration components must be non-negative")
    
    if seconds >= 60 or minutes >= 60:
        raise ValueError("Minutes and seconds must be less than 60")
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds = remaining_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    parts_list = []
    if days > 0:
        parts_list.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts_list.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts_list.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0:
        parts_list.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    if not parts_list:
        return "0 seconds"
    
    if len(parts_list) == 1:
        return parts_list[0]
    
    return ', '.join(parts_list[:-1]) + ' and ' + parts_list[-1]

if __name__ == '__main__':
    print(format_duration("01:02:03"))
    print(format_duration("00:00:00"))
    print(format_duration("172:05:05"))
    print(format_duration("00:01:00"))
    print(format_duration("01:00:00"))
    print(format_duration("00:00:01"))