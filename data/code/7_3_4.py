def convert_duration(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    
    parts_result = []
    if days > 0:
        if days == 1:
            parts_result.append("1 Day")
        else:
            parts_result.append(f"{days} Days")
    if hours > 0:
        if hours == 1:
            parts_result.append("1 Hour")
        else:
            parts_result.append(f"{hours} Hours")
    if minutes > 0:
        if minutes == 1:
            parts_result.append("1 Minute")
        else:
            parts_result.append(f"{minutes} Minutes")
    if seconds > 0:
        if seconds == 1:
            parts_result.append("1 Second")
        else:
            parts_result.append(f"{seconds} Seconds")
    
    if not parts_result:
        return "0 Seconds"
    
    if len(parts_result) == 1:
        return parts_result[0]
    else:
        return ", ".join(parts_result[:-1]) + " and " + parts_result[-1]

if __name__ == '__main__':
    print(convert_duration("01:02:03"))
    print(convert_duration("25:00:00"))
    print(convert_duration("00:00:00"))
    print(convert_duration("00:01:01"))
    print(convert_duration("48:00:00"))