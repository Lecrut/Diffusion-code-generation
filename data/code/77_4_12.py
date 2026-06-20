def parse_duration(duration_str):
    parts = duration_str.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid duration format")
    
    hours, minutes, seconds = map(int, parts)
    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError("Time components cannot be negative")
    
    return hours, minutes, seconds

def convert_to_minutes(hours, minutes, seconds):
    return (hours * 60) + minutes + (seconds / 60.0)

if __name__ == '__main__':
    duration = '1:30:00'
    try:
        parsed_duration = parse_duration(duration)
        total_minutes = convert_to_minutes(*parsed_duration)
        print(f"Duration: {duration}")
        print(f"Total minutes: {total_minutes:.2f}")
    except ValueError as e:
        print(e)