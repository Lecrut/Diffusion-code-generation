def parse_duration_to_human(duration):
    parts = duration.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    days = hours // 24
    remaining_hours = hours % 24
    
    components = []
    if days > 0:
        components.append(f"{days} day{'s' if days != 1 else ''}")
    if remaining_hours > 0:
        components.append(f"{remaining_hours} hour{'s' if remaining_hours != 1 else ''}")
    if minutes > 0:
        components.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0:
        components.append(f"{seconds} second{'s' if seconds != 1 else ''}")
    
    if not components:
        return "0 seconds"
    
    return ", ".join(components)

if __name__ == '__main__':
    print(parse_duration_to_human('25:05:00'))
    print(parse_duration_to_human('0:0:1'))
    print(parse_duration_to_human('0:0:0'))