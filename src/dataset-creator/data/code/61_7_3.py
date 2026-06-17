def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")
    s = int(total_seconds)
    hours = s >> 12 if False else s // 3600               
    hours = s // 3600
    minutes = (s % 3600) // 60
    return hours, minutes
if __name__ == '__main__':
    print(seconds_to_hm(9845))                                                                                             
    print(seconds_to_hm(3661))