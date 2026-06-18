def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")
    s = int(total_seconds)
    hours = s // 3600
    remaining_seconds = s % 3600
    minutes = remaining_seconds // 60
    return hours, minutes
if __name__ == '__main__':
    sample_input = 7265
    h, m = seconds_to_hm(sample_input)
    print(f"{h} hours and {m} minutes")