def compute_seconds_delta(epoch_a: int, epoch_b: int) -> int:
    delta = epoch_b - epoch_a
    if delta < 0:
        delta = -delta
    return delta

if __name__ == '__main__':
    start_time = 1625097600
    end_time = 1625101200
    total_seconds = compute_seconds_delta(start_time, end_time)
    print(total_seconds)