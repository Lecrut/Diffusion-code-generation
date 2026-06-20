def format_duration(duration: str) -> str:
    hours, minutes, seconds = map(int, duration.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    hours_remaining = remainder // 3600
    remainder = remainder % 3600
    minutes_remaining = remainder // 60
    seconds_remaining = remainder % 60

    parts = []
    if days > 0:
        parts.append(f"{days} Days")
    if hours_remaining > 0:
        parts.append(f"{hours_remaining} Hours")
    if minutes_remaining > 0:
        parts.append(f"{minutes_remaining} Minutes")
    if seconds_remaining > 0:
        parts.append(f"{seconds_remaining} Seconds")
    
    return ", ".join(parts) if parts else "0 Seconds"

if __name__ == '__main__':
    print(format_duration("26:00:01"))
    print(format_duration("00:00:00"))
    print(format_duration("00:00:05"))