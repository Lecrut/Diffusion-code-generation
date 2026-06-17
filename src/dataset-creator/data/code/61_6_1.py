def convert_time_to_seconds(time_in_hours):
    if not isinstance(time_in_hours, (int, float)):
        raise TypeError("Input must be an integer or a floating-point number.")
    if time_in_hours < 0:
        raise ValueError("Time cannot be negative.")
    return int(time_in_hours * 3600)
if __name__ == '__main__':
    sample_values = [1, 24, 75.5]
    for val in sample_values:
        result_seconds = convert_time_to_seconds(val)
        print(f"{val} hours is {result_seconds} seconds.")