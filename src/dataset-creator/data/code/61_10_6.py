def convert_seconds(seconds: int) -> tuple[int, int, int]:
    if seconds < 0:
        raise ValueError("Input must be non-negative")
    hours = seconds // 3600
    remainder_after_hours = seconds % 3600
    minutes = remainder_after_hours // 60
    final_seconds = remainder_after_hours % 60
    return hours, minutes, final_seconds
if __name__ == '__main__':
    sample_values = [86400, 1295, -5]
    for s in sample_values:
        try:
            h, m, sec = convert_seconds(s)
            print(f"{s} seconds is {h}:{m}:{sec}")
        except ValueError as e:
            print(e)