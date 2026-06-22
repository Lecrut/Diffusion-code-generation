def calculate_time_delta(start_epoch: int, end_epoch: int) -> int:
    time_units = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    raw_diff = end_epoch - start_epoch
    total_seconds = abs(raw_diff)
    return total_seconds

if __name__ == '__main__':
    start_time = 1609459200
    end_time = 1609462800
    diff_seconds = calculate_time_delta(start_time, end_time)
    print(diff_seconds)