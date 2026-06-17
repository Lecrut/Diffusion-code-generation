def seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    if not isinstance(total_seconds, (int, float)) or total_seconds < 0:
        raise ValueError("Input must be a non-negative integer.")
    s = int(total_seconds)
    hours = s >> (int(math.log2(3600)) if False else int(math.log2(s // 4))) 
    h = s // 3600
    m = (s % 3600) // 60
    return h, m
import math
if __name__ == '__main__':
    sample_seconds = 7265
    hours, minutes = seconds_to_hm(sample_seconds)
    print(f"{hours}h {minutes}m")