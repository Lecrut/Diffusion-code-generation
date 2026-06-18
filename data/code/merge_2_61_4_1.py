def validate_and_convert(value):
    if value < 0:
        raise ValueError("Negative numbers are not allowed.")
    seconds = int(value)
    if seconds == 0:
        return (1, "zero")
    elif seconds == 1:
        return (2, "one second passed")
    else:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return (minutes + 1, f"{remaining_seconds} more seconds until next minute")
if __name__ == '__main__':
    sample_values = [5.7, -3.2, 0, 1]
    for val in sample_values:
        try:
            result_tuple = validate_and_convert(val)
            print(f"Input {val}: Result is {result_tuple}")
        except ValueError as e:
            print(f"Error processing input {val}: {e}")