import time
def seconds_to_hms(seconds: int) -> tuple[int, int]:
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer or float representing seconds.")
    try:
        total_seconds = round(float(seconds))
        if total_seconds < 0:
            raise ValueError("Seconds cannot be negative.")
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) / 60)
    except OverflowError:
        raise OverflowError("Input value is too large to convert safely.")
def seconds_to_hms_static(seconds: int | float) -> tuple[int, int]:
    return seconds_to_hms(int(round(float(seconds))))
if __name__ == '__main__':
    sample_seconds = 7265
    try:
        h_m_s_tuple = seconds_to_hms_static(sample_seconds)
        print(f"Input: {sample_seconds} seconds")
        print("Output:")
        print(f"Hours: {h_m_s_tuple[0]}")
        print(f"Minutes: {h_m_s_tuple[1]}")
    except (TypeError, ValueError, OverflowError) as e:
        error_type = type(e).__name__
        print(f"Conversion failed with an exception of type '{error_type}'. Message: {e}")