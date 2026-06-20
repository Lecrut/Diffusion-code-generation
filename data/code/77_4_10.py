def parse_duration_string(duration_str):
    parts = duration_str.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid duration format")
    
    hours, minutes, seconds = map(int, parts)
    if any(part < 0 for part in [hours, minutes, seconds]):
        raise ValueError("Time components cannot be negative")
    
    return hours, minutes, seconds

def convert_to_minutes(hours, minutes, seconds):
    total_minutes = (hours * 60) + minutes + (seconds / 60.0)
    return total_minutes

if __name__ == '__main__':
    duration_str = '1:30:00'
    try:
        hours, minutes, seconds = parse_duration_string(duration_str)
        total_minutes = convert_to_minutes(hours, minutes, seconds)
        print(f"Duration: {duration_str}")
        print(f"Total minutes: {total_minutes:.2f}")
    except ValueError as e:
        print(e)