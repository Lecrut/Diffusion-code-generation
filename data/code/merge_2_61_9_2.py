def convert_seconds_to_hm(seconds: int) -> tuple[int, int]:
    if not isinstance(seconds, (int, float)):
        raise TypeError("Input must be an integer representing seconds.")
    try:
        total_minutes = int(round(seconds / 60))
        remaining_seconds = round((seconds % 1) * 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return (hours, minutes), remaining_seconds if seconds != int(seconds) else None
    except OverflowError:
        raise ValueError("Input value is too large to convert.")
if __name__ == '__main__':
    sample_input = 3725.4
    try:
        result_data, extra_sec = convert_seconds_to_hm(sample_input)
        hours, minutes = result_data
        print(f"Hours: {hours}")
        print(f"Minutes: {minutes}")
        if extra_sec is not None:
            print(f"Remaining Seconds (fractional): {extra_sec:.2f}")
    except Exception as e:
        print(f"Error occurred: {e}")