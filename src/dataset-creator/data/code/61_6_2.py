def convert_time_to_seconds(hours: int, minutes: int, seconds_input: float) -> int:
    if not isinstance(hours, (int, float)) or not isinstance(minutes, int):
        raise TypeError("Hours must be an integer or float; minutes must be an integer.")
    if hours < 0 or minutes < 0:
        raise ValueError("Hours and minutes cannot be negative.")
    total_seconds = int(hours * 3600 + minutes * 60 + seconds_input)
    return total_seconds
if __name__ == '__main__':
    h, m, s = 123456789.0, 987654, 0.99
    result_seconds = convert_time_to_seconds(h, m, s)
    print(f"Total seconds: {result_seconds}")