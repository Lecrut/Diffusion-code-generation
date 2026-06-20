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
    duration_str = '1:30:00'
    try:
        hours, minutes, seconds = parse_duration(duration_str)
        total_minutes = convert_to_minutes(hours, minutes, seconds)
        print(f"Duration: {duration_str}")
        print(f"Total minutes: {total_minutes:.2f}")
    except ValueError as e:
        print(e)