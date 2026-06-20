def format_duration(duration):
    hours, minutes, seconds = map(int, duration.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    parts = []
    if days > 0:
        parts.append(f'{days} day{"s" if days != 1 else ""}')
    if hours > 0:
        parts.append(f'{hours} hour{"s" if hours != 1 else ""}')
    if minutes > 0:
        parts.append(f'{minutes} minute{"s" if minutes != 1 else ""}')
    if seconds > 0:
        parts.append(f'{seconds} second{"s" if seconds != 1 else ""}')
    if not parts:
        return '0 seconds'
    return ', '.join(parts)

if __name__ == '__main__':
    result = format_duration('26:00:00')
    print(result)