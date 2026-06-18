def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")
    return divmod(int(round(total_seconds)), 3600)
def convert_to_hm(seconds: int | float) -> tuple[int, int]:
    total_hours = seconds // 3600
    remaining_seconds_for_minutes = (seconds % 3600) // 60
    return total_hours, remaining_seconds_for_minutes
if __name__ == '__main__':
    sample_input = 125478.9
    hours, minutes = convert_to_hm(sample_input)
    print(f"{hours}h {minutes}m")