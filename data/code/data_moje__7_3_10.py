def convert_duration(duration_str):
    parts = duration_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])

    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    result = []
    if days > 0:
        result.append(f"{days} days")
    if hours > 0:
        result.append(f"{hours} hours")
    if minutes > 0:
        result.append(f"{minutes} minutes")
    if seconds > 0:
        result.append(f"{seconds} seconds")
    
    if not result:
        return "0 seconds"
    
    return ", ".join(result)

if __name__ == '__main__':
    print(convert_duration("25:05:30"))
    print(convert_duration("00:00:00"))
    print(convert_duration("00:00:45"))
    print(convert_duration("48:00:00"))