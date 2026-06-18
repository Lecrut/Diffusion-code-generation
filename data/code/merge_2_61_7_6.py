def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    if total_seconds < 0:
        raise ValueError("Total seconds must be non-negative")
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds % 3600
    minutes = remaining_after_hours // 60
    return hours, minutes
if __name__ == '__main__':
    sample_value_1 = 7265
    sample_value_2 = 900
    h1, m1 = seconds_to_hm(sample_value_1)
    print(f"{sample_value_1} seconds -> {h1} hours and {m1} minutes")
    h2, m2 = seconds_to_hm(sample_value_2)
    print(f"{sample_value_2} seconds -> {h2} hours and {m2} minutes")