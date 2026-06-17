import time
def convert_seconds_to_hm(seconds: int) -> tuple[int, int]:
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer or float representing seconds.")
    try:
        total_seconds = int(round(float(seconds)))
        if total_seconds < 0:
            raise ValueError("Seconds cannot be negative.")
        hours = total_seconds // 3600
        remaining_minutes = (total_seconds % 3600) // 60
        return hours, remaining_minutes
    except OverflowError:
        raise ValueError("Input value is too large to convert safely.")
if __name__ == '__main__':
    sample_input = 7265.4
    try:
        h, m = convert_seconds_to_hm(sample_input)
        print(f"{h} hours and {m} minutes")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")