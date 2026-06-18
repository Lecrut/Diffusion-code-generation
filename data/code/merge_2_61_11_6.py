from typing import Tuple
def format_time(total_seconds: int) -> Tuple[int, int, int]:
    if not isinstance(total_seconds, int):
        raise TypeError("Input must be an integer.")
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return (hours, minutes, seconds)
if __name__ == '__main__':
    sample_inputs: list[int] = [0, 125478, -999, 3661, 9876543210]
    for input_val in sample_inputs:
        try:
            result = format_time(input_val)
            print(f"Input: {input_val} -> Hours: {result[0]}, Minutes: {result[1]}, Seconds: {result[2]}")
        except (ValueError, TypeError):
            print(f"Input: {input_val} -> Error occurred during conversion.")