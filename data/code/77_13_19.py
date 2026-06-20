MINUTES_PER_HOUR = 60

def convert_to_minutes(time_str):
    parts = time_str.split(':')
    if len(parts) != 2:
        raise ValueError("Incorrect format")
    hours = int(parts[0])
    minutes = int(parts[1])
    if not (0 <= hours < 24 and 0 <= minutes < MINUTES_PER_HOUR):
        raise ValueError("Time values out of range")
    return hours * MINUTES_PER_HOUR + minutes

if __name__ == '__main__':
    sample_input = "1:30"
    try:
        total_minutes = convert_to_minutes(sample_input)
        print(total_minutes)
    except ValueError as e:
        print(f"Error: {e}")