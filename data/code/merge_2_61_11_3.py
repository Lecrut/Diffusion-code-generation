from typing import Tuple
def convert_seconds_to_time(total_seconds: int) -> Tuple[int, int, int]:
    if not isinstance(total_seconds, int) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return (hours, minutes, seconds)
if __name__ == '__main__':
    sample_inputs: list[int] = [0, 12345, 86400, -10]
    for input_val in sample_inputs:
        try:
            h, m, s = convert_seconds_to_time(input_val)
            print(f"Input: {input_val} seconds -> {h} hours, {m} minutes, {s} seconds")
        except ValueError as e:
            print(f"Error for input {input_val}: {e}")