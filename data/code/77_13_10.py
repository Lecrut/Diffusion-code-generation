def convert_to_minutes(time_str):
    parts = time_str.split(':')
    if len(parts) != 2:
        raise ValueError("Incorrect format")
    hours, minutes = map(int, parts)
    if not (0 <= hours <= 23 and 0 <= minutes <= 59):
        raise ValueError("Time values out of range")
    return hours * 60 + minutes

if __name__ == '__main__':
    sample_input = "1:30"
    try:
        result = convert_to_minutes(sample_input)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")