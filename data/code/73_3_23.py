def compute_epoch_delta(first_epoch: int, second_epoch: int) -> int:
    if not isinstance(first_epoch, (int, float)):
        raise ValueError("first_epoch must be numeric")
    if not isinstance(second_epoch, (int, float)):
        raise ValueError("second_epoch must be numeric")
    diff = float(first_epoch) - float(second_epoch)
    return abs(int(diff))

if __name__ == '__main__':
    epoch_start = 1700000000
    epoch_end = 1700000055
    delta_seconds = compute_epoch_delta(epoch_start, epoch_end)
    print(delta_seconds)