def seconds_to_hm(seconds: int) -> tuple[int, int]:
    if not isinstance(seconds, int):
        raise TypeError("Input must be an integer")
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    return hours, minutes
if __name__ == '__main__':
    test_cases = [86400, 900719925, -3661]                                                                                                                        
    for s in test_cases:
        h, m = seconds_to_hm(s)
        print(f"{s} seconds -> {h} hours and {m} minutes")