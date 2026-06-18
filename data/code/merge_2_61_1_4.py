from typing import Tuple
def seconds_to_hm(total_seconds: int) -> Tuple[int, int]:
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    return (hours, minutes)
if __name__ == '__main__':
    sample_value: int = 7265
    hours, minutes = seconds_to_hm(sample_value)
    print(f"{sample_value} seconds is {hours} hour(s) and {minutes} minute(s).")