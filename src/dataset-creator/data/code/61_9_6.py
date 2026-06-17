import time
def seconds_to_hm(seconds: int) -> tuple[int, int]:
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer or float representing seconds.")
    try:
        total_seconds = int(round(float(seconds)))
    except ValueError:
        raise ValueError(f"Invalid input type for conversion. Expected numeric value, got {type(seconds).__name__}.")
    hours = total_seconds // 3600
    remaining_minutes = (total_seconds % 3600) // 60
    return int(hours), int(remaining_minutes)
if __name__ == '__main__':
    sample_input = 7265.4
    try:
        hours, minutes = seconds_to_hm(sample_input)
        print(f"{hours} hours and {minutes} minutes")
        bad_input = "invalid"
        result = seconds_to_hm(bad_input)
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")