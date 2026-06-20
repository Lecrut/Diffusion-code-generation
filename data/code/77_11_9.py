def time_to_minutes(time_str):
    try:
        h, m = map(int, time_str.split(':')[:2])
        if not (0 <= h < 24 and 0 <= m < 60):
            raise ValueError("Time components out of valid range")
        total_minutes = h * 60 + m
        return total_minutes
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid time format. Expected HH:MM. Got '{time_str}': {e}")

if __name__ == '__main__':
    test_times = [
        "00:00",
        "23:59",
        "01:30",
        "12:00",
        "invalid_time"
    ]
    for time_str in test_times:
        try:
            print(f"{time_str} -> {time_to_minutes(time_str)} minutes")
        except ValueError as e:
            print(e)