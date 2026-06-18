def validate_and_compute(seconds):
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be a number.")
    if seconds < 0:
        return None
    if seconds == 0:
        return (0, 0)
    int_seconds = int(seconds)
    remaining_decimal = round((seconds - int_seconds) * 100, 2)
    return (int_seconds, remaining_decimal)
if __name__ == '__main__':
    sample_values = [3.5, 4, -1, 0]
    for val in sample_values:
        result = validate_and_compute(val)
        print(f"Input {val}: {result}")