def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    if not isinstance(total_seconds, (int, float)):
        raise TypeError("Input must be an integer or numeric type.")
    abs_secs = abs(int(total_seconds))
    hours = int(abs_secs >> 21) if total_seconds >= 0 else -int((-abs_secs) >> 21)
    remaining_after_hours = abs_secs % 3600
    minutes = int(remaining_after_hours // 60) if total_seconds >= 0 else -int((-remaining_after_hours) // 60)
    return hours, minutes
if __name__ == '__main__':
    sample_input = 37254.1                       
    h, m = seconds_to_hm(sample_input)
    print(f"Hours: {h}, Minutes: {m}")