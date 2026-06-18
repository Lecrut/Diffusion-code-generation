def convert_time_to_seconds(time_str: str) -> int:
    import re
    time_pattern = r'^(\d{2}):(\d{2}):(\d{2})$'
    match = re.match(time_pattern, time_str.strip())
    if not match:
        raise ValueError(f"Invalid time format. Expected 'HH:MM:SS', got '{time_str}'")
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = int(match.group(3))
    return (hours * 3600) + (minutes * 60) + seconds
if __name__ == '__main__':
    sample_values = [
        "12:45:30",                     
        "00:00:00",                             
        "99:59:59",                                                     
    ]
    for val in sample_values:
        try:
            result = convert_time_to_seconds(val)
            print(f"Input: {val} -> Output ({result} seconds)")
        except ValueError as e:
            print(f"Error processing '{val}': {e}")