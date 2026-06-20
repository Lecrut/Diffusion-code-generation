HOURS_TO_MINUTES = 60

def convert_to_minutes(time_str):
    parts = time_str.split(':')
    if len(parts) != 2:
        raise ValueError("Incorrect format")
    hours = int(parts[0])
    minutes = int(parts[1])
    if not (0 <= hours < 24 and 0 <= minutes < 60):
        raise ValueError("Time values out of range")
    total_minutes = hours * HOURS_TO_MINUTES + minutes
    return total_minutes

if __name__ == '__main__':
    sample_input = "1:30"
    try:
        result = convert_to_minutes(sample_input)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")