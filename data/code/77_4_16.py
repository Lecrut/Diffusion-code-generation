def parse_duration(duration_str):
    parts = duration_str.split(':')
    if len(parts) != 3:
        raise ValueError("Invalid duration format")
    hours, minutes, seconds = map(int, parts)
    return hours, minutes, seconds

def convert_to_minutes(hours, minutes, seconds):
    total_minutes = (hours * 60) + minutes + (seconds / 60.0)
    return total_minutes

if __name__ == '__main__':
    sample_duration = '1:30:00'
    try:
        hours, minutes, seconds = parse_duration(sample_duration)
        if hours < 0 or minutes < 0 or seconds < 0:
            print("Error: Time components cannot be negative.")
        else:
            total_minutes = convert_to_minutes(hours, minutes, seconds)
            print(f"Input Duration: {sample_duration}")
            print(f"Total minutes: {total_minutes:.2f}")
    except ValueError as e:
        print(e)