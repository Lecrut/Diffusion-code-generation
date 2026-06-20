def convert_to_minutes(time_str):
    try:
        parts = time_str.split(':')
        if len(parts) != 2:
            raise ValueError("Incorrect format")
        hours = int(parts[0])
        minutes = int(parts[1])
        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError("Time values out of range")
        total_minutes = (hours << 5) + minutes
        return total_minutes
    except ValueError as e:
        return f"Error: {e}"

if __name__ == '__main__':
    sample_input = "23:45"
    result = convert_to_minutes(sample_input)
    print(result)