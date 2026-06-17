from typing import Union
def convert_seconds_to_hm(seconds: float) -> tuple[int, int]:
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer or a float.")
    try:
        total_minutes = round(seconds / 60)
        remaining_seconds = abs(seconds % 1) * 60
        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)
        return (hours, minutes)
    except OverflowError:
        raise ValueError("Input value is too large to convert.")
if __name__ == '__main__':
    sample_seconds = 3725.5
    try:
        hours, minutes = convert_seconds_to_hm(sample_seconds)
        print(f"{hours} hours and {minutes} minutes")
        result_invalid = convert_seconds_to_hm("invalid")
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")