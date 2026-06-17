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
    sample_input: int = 98475
    hours, minutes, seconds = convert_seconds_to_time(sample_input)
    print(f"{sample_input} seconds is {hours} hours, {minutes} minutes, and {seconds} seconds.")