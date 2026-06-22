def time_to_human_readable(time_string):
    try:
        hours, minutes, seconds = map(int, time_string.split(':'))
        total_seconds = hours * 3600 + minutes * 60 + seconds
    except (ValueError, IndexError):
        raise ValueError("Invalid time format. Use 'HH:MM:SS'.")

    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    seconds = remaining % 60

    parts = []
    if days > 0:
        parts.append(f"{days} day" + ("s" if days != 1 else ""))
    if hours > 0:
        parts.append(f"{hours} hour" + ("s" if hours != 1 else ""))
    if minutes > 0:
        parts.append(f"{minutes} minute" + ("s" if minutes != 1 else ""))
    if seconds > 0 or not parts:
        parts.append(f"{seconds} second" + ("s" if seconds != 1 else ""))

    return ", ".join(parts)

if __name__ == '__main__':
    sample_time = "01:45:30"
    print(time_to_human_readable(sample_time))
    sample_time_2 = "25:00:00"
    print(time_to_human_readable(sample_time_2))
    sample_time_3 = "00:00:01"
    print(time_to_human_readable(sample_time_3))