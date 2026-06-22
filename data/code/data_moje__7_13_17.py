def time_string_to_human_readable(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid time format. Expected HH:MM:SS")
    
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    result_parts = []
    if days > 0:
        result_parts.append(f"{days} days" if days != 1 else "1 day")
    if hours > 0:
        result_parts.append(f"{hours} hours" if hours != 1 else "1 hour")
    if minutes > 0:
        result_parts.append(f"{minutes} minutes" if minutes != 1 else "1 minute")
    if seconds > 0 or not result_parts:
        result_parts.append(f"{seconds} seconds" if seconds != 1 else "1 second")
    
    return ", ".join(result_parts)

if __name__ == '__main__':
    sample_input_1 = "00:00:00"
    sample_input_2 = "01:30:15"
    sample_input_3 = "25:45:30"
    sample_input_4 = "100:00:05"
    
    print(time_string_to_human_readable(sample_input_1))
    print(time_string_to_human_readable(sample_input_2))
    print(time_string_to_human_readable(sample_input_3))
    print(time_string_to_human_readable(sample_input_4))