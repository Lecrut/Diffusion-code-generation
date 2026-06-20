import math

def time_string_to_seconds(time_str: str) -> int:
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_human_readable(total_seconds: int) -> str:
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    hours = remaining // 3600
    remaining = remaining % 3600
    minutes = remaining // 60
    seconds = remaining % 60

    parts = []
    if days > 0:
        parts.append(f"{days} day" if days == 1 else f"{days} days")
    if hours > 0:
        parts.append(f"{hours} hour" if hours == 1 else f"{hours} hours")
    if minutes > 0:
        parts.append(f"{minutes} minute" if minutes == 1 else f"{minutes} minutes")
    if seconds > 0:
        parts.append(f"{seconds} second" if seconds == 1 else f"{seconds} seconds")
    
    if not parts:
        return "0 seconds"
    
    return ", ".join(parts)

def convert_time_format(time_str: str) -> str:
    total_seconds = time_string_to_seconds(time_str)
    return seconds_to_human_readable(total_seconds)

if __name__ == '__main__':
    sample_time = "93:42:16"
    result = convert_time_format(sample_time)
    print(result)