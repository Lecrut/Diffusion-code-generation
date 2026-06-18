import math
def convert_seconds_to_hm(seconds: int) -> tuple[int, int]:
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer or a numeric type.")
    try:
        total_minutes = math.floor(abs(seconds) / 60)
        remaining_seconds = abs(int(seconds)) % 60
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return (hours, minutes) if seconds >= 0 else (-hours, -minutes)
    except OverflowError:
        raise ValueError("Input value is too large to be converted.")
if __name__ == '__main__':
    sample_seconds = 3725
    try:
        hours, minutes = convert_seconds_to_hm(sample_seconds)
        print(f"{sample_seconds} seconds equals {hours} hour(s) and {minutes} minute(s).")
        invalid_inputs = [None, "invalid", [], {}, True]
        for val in invalid_inputs:
            try:
                result = convert_seconds_to_hm(val)
            except (TypeError, ValueError) as e:
                print(f"Error processing input {val}: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")