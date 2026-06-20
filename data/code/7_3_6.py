def format_duration(duration_str):
    parts = duration_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    days = 0
    if hours >= 24:
        days = hours // 24
        hours = hours % 24
    
    units = []
    if days > 0:
        units.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        units.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        units.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0 or not units:
        units.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    return ', '.join(units)

if __name__ == '__main__':
    result = format_duration("25:00:01")
    print(result)