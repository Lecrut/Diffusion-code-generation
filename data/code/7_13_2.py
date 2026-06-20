def convert_time_string(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in 'HH:MM:SS' format")
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
    result_parts = []
    if days > 0:
        if days == 1:
            result_parts.append("1 day")
        else:
            result_parts.append(f"{days} days")
    if hours > 0:
        if hours == 1:
            result_parts.append("1 hour")
        else:
            result_parts.append(f"{hours} hours")
    if minutes > 0:
        if minutes == 1:
            result_parts.append("1 minute")
        else:
            result_parts.append(f"{minutes} minutes")
    if seconds > 0 or not result_parts:
        if seconds == 1:
            result_parts.append("1 second")
        else:
            result_parts.append(f"{seconds} seconds")
    return ", ".join(result_parts)

if __name__ == '__main__':
    print(convert_time_string("00:00:00"))
    print(convert_time_string("01:02:03"))
    print(convert_time_string("24:00:00"))
    print(convert_time_string("48:30:15"))
    print(convert_time_string("100:00:00"))