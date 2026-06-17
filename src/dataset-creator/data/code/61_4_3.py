def calculate_duration(seconds):
    if seconds < 0:
        raise ValueError("Duration cannot be negative.")
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    final_seconds = remaining_seconds % 60
    return (hours, minutes, final_seconds)
if __name__ == '__main__':
    sample_input = -5
    try:
        result = calculate_duration(sample_input)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")