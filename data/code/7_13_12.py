def time_string_to_seconds(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time string must be in 'HH:MM:SS' format")
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_human_readable(total_seconds):
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative")
    days = total_seconds // 86400
    remainder = total_seconds % 86400
    hours = remainder // 3600
    remainder %= 3600
    minutes = remainder // 60
    seconds = remainder % 60
    parts = []
    if days > 0:
        parts.append(f"{days} days" if days != 1 else "1 day")
    if hours > 0:
        parts.append(f"{hours} hours" if hours != 1 else "1 hour")
    if minutes > 0:
        parts.append(f"{minutes} minutes" if minutes != 1 else "1 minute")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} seconds" if seconds != 1 else "1 second")
    return ", ".join(parts)

def convert_time_to_human_readable(time_str):
    total_seconds = time_string_to_seconds(time_str)
    return seconds_to_human_readable(total_seconds)

if __name__ == '__main__':
    sample_time_1 = "00:01:30"
    result_1 = convert_time_to_human_readable(sample_time_1)
    print(f"Input: {sample_time_1} -> Output: {result_1}")
    
    sample_time_2 = "25:45:10"
    result_2 = convert_time_to_human_readable(sample_time_2)
    print(f"Input: {sample_time_2} -> Output: {result_2}")
    
    sample_time_3 = "1:02:03"
    result_3 = convert_time_to_human_readable(sample_time_3)
    print(f"Input: {sample_time_3} -> Output: {result_3}")
    
    sample_time_4 = "00:00:01"
    result_4 = convert_time_to_human_readable(sample_time_4)
    print(f"Input: {sample_time_4} -> Output: {result_4}")
    
    sample_time_5 = "00:00:00"
    result_5 = convert_time_to_human_readable(sample_time_5)
    print(f"Input: {sample_time_5} -> Output: {result_5}")