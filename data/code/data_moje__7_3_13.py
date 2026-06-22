def format_duration(duration_str):
    hours, minutes, seconds = map(int, duration_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60

    parts = []
    if days > 0:
        parts.append(f"{days} days")
    if hours > 0:
        parts.append(f"{hours} hours")
    if minutes > 0:
        parts.append(f"{minutes} minutes")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} seconds")

    return ", ".join(parts)

if __name__ == '__main__':
    print(format_duration('25:01:05'))