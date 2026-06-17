from typing import Tuple
def convert_seconds_to_time(total_seconds: int) -> Tuple[int, int, int]:
    if not isinstance(total_seconds, int):
        raise TypeError("Input must be an integer.")
    if total_seconds < 0:
        return (-total_seconds // 3600, -(-total_seconds // 60) % 60, -(total_seconds % 60))
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    seconds = remaining_after_hours % 60
    return (hours, minutes, seconds)
if __name__ == '__main__':
    sample_inputs = [0, 12345, 86400, -90]
    for sec in sample_inputs:
        try:
            h, m, s = convert_seconds_to_time(sec)
            print(f"{sec} seconds -> {h}:{m:02d}:{s:02d}")
        except TypeError as e:
            print(f"Error with input {sec}: {e}")