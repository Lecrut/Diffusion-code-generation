def calculate_duration(seconds: int) -> tuple[int]:
    if seconds < 0:
        raise ValueError("Duration cannot be negative.")
    result = (seconds,)
    return result
if __name__ == '__main__':
    sample_input = -5
    try:
        output = calculate_duration(sample_input)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")