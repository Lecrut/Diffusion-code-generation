def format_duration(time_string):
    hours, minutes, seconds = map(int, time_string.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    parts = []
    if days > 0:
        parts.append(f"{days} Day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} Hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} Minute{'s' if minutes != 1 else ''}")
    if seconds > 0:
        parts.append(f"{seconds} Second{'s' if seconds != 1 else ''}")
    if not parts:
        return "0 Seconds"
    return ", ".join(parts)

if __name__ == '__main__':
    print(format_duration("01:00:00"))
    print(format_duration("25:30:15"))
    print(format_duration("00:00:01"))
    print(format_duration("2:05:03"))