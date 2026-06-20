def parse_time_to_seconds(time_str):
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_human_readable(total_seconds):
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    result_parts = []
    if days > 0:
        result_parts.append(f"{days} days")
    if hours > 0:
        result_parts.append(f"{hours} hours")
    if minutes > 0:
        result_parts.append(f"{minutes} minutes")
    if seconds > 0 or not result_parts:
        result_parts.append(f"{seconds} seconds")
    return ", ".join(result_parts)

if __name__ == '__main__':
    test_cases = [
        "01:00:00",
        "00:00:01",
        "25:30:15",
        "99:59:59",
        "00:00:00"
    ]
    for time_str in test_cases:
        total_secs = parse_time_to_seconds(time_str)
        human_readable = seconds_to_human_readable(total_secs)
        print(f"{time_str} -> {human_readable}")