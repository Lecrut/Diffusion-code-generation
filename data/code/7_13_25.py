def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_human_readable(total_seconds):
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days > 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

    return ', '.join(parts)

def convert_time_format(time_str):
    total_seconds = time_to_seconds(time_str)
    human_readable = seconds_to_human_readable(total_seconds)
    return human_readable

if __name__ == '__main__':
    sample_time = '48:30:15'
    result = convert_time_format(sample_time)
    print(result)