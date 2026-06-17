def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")
    hours = total_seconds // 3600
    remaining_after_hours = total_seconds - (hours * 3600)
    minutes = remaining_after_hours // 60
    return int(hours), int(minutes)
if __name__ == '__main__':
    sample_input = 1259847.0                                                                  
    test_val = int(3 * 60 * 60 + 45) 
    h, m = seconds_to_hm(test_val)
    print(f"Hours: {h}, Minutes: {m}")