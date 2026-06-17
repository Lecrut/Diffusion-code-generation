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
    sample_inputs: list[int] = [0, 12345, 86400, 999999999]
    for sec in sample_inputs:
        h, m, s = convert_seconds_to_time(sec)
        print(f"{sec} seconds -> {h}:{m:02d}:{s:02d}")