def format_seconds(total_seconds):
    total_seconds = int(total_seconds)
    if total_seconds < 0:
        return f"-{format_seconds(-total_seconds)}"
    if total_seconds == 0:
        return "0 seconds"
    
    units = [
        ("year", 31536000),
        ("month", 2592000),
        ("week", 604800),
        ("day", 86400),
        ("hour", 3600),
        ("minute", 60),
        ("second", 1)
    ]
    
    parts = []
    for unit_name, unit_seconds in units:
        if total_seconds >= unit_seconds:
            count = total_seconds // unit_seconds
            total_seconds %= unit_seconds
            plural = unit_name if count == 1 else unit_name + "s"
            parts.append(f"{count} {plural}")
            if total_seconds == 0:
                break
    
    return ", ".join(parts)

if __name__ == '__main__':
    print(format_seconds(3661))
    print(format_seconds(90))
    print(format_seconds(86400))
    print(format_seconds(5432109))