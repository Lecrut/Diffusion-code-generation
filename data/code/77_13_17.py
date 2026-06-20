def convert_to_minutes(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Incorrect format")
    hours, minutes, seconds = map(int, parts)
    if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
        raise ValueError("Time values out of range")
    return hours * 60 + minutes + seconds / 60

if __name__ == '__main__':
    sample_input = "1:30:15"
    try:
        total_minutes = convert_to_minutes(sample_input)
        print(total_minutes)
    except ValueError as e:
        print(f"Error: {e}")