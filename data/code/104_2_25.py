import time

def calculate_seconds_difference(start_time: int, end_time: int) -> int:
    if not isinstance(start_time, int) or not isinstance(end_time, int):
        raise ValueError("Both arguments must be integers")
    delta = end_time - start_time
    return delta if delta >= 0 else -delta

if __name__ == '__main__':
    t1 = 1609459200
    t2 = 1609462800
    seconds_elapsed = calculate_seconds_difference(t1, t2)
    print(seconds_elapsed)