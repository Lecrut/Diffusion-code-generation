def duration_to_human_readable(duration: str) -> str:
    parts = duration.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])

    days = hours // 24
    remaining_hours = hours % 24

    components = []

    if days > 0:
        components.append(f"{days} Day")
    
    if remaining_hours > 0:
        components.append(f"{remaining_hours} Hour")
    
    if minutes > 0:
        components.append(f"{minutes} Minute")
    
    if seconds > 0:
        components.append(f"{seconds} Second")

    if not components:
        return "0 Second"
    
    return ", ".join(components)

if __name__ == '__main__':
    result = duration_to_human_readable("25:01:05")
    print(result)