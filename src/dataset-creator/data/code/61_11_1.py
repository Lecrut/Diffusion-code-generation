def convert_seconds_to_time(total_seconds: int) -> tuple[int, int, int]:
    if not isinstance(total_seconds, int) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")
    hours = total_seconds // 3600
    remainder_after_hours = total_seconds % 3600
    minutes = remainder_after_hours // 60
    seconds = remainder_after_hours % 60
    return hours, minutes, seconds
if __name__ == '__main__':
    sample_input: int = 98475
    h, m, s = convert_seconds_to_time(sample_input)
    print(f"{h} hours, {m} minutes, {s} seconds")