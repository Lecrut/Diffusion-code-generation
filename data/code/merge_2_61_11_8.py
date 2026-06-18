from typing import Tuple
def convert_seconds_to_time(total_seconds: int) -> Tuple[int, int, int]:
    if not isinstance(total_seconds, int):
        raise TypeError(f"Expected int, got {type(total_seconds).__name__}")
    if total_seconds < 0:
        raise ValueError("Total seconds cannot be negative.")
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return (hours, minutes, seconds)
if __name__ == '__main__':
    sample_inputs: list[int] = [0, -5, 12345, 86400, 999999999]
    for sec in sample_inputs:
        try:
            h, m, s = convert_seconds_to_time(sec)
            print(f"{sec} seconds -> {h} hours, {m} minutes, {s} seconds")
        except (TypeError, ValueError) as e:
            print(f"Error for input {sec}: {e}")