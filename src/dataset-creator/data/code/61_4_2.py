def calculate_duration(seconds):
    if seconds < 0:
        raise ValueError("Duration cannot be negative.")
    if seconds == 0:
        return (0, 0)
    total_minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    return (total_minutes, remaining_seconds)
if __name__ == '__main__':
    sample_values = [5.75, -2.3, 0, 1]
    for val in sample_values:
        try:
            result = calculate_duration(val)
            print(f"Input {val}: Result is {result}")
        except ValueError as e:
            print(f"Error for input {val}: {e}")