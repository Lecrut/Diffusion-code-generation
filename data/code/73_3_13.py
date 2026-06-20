def validate_timestamps(timestamp1, timestamp2):
    if not isinstance(timestamp1, int) or not isinstance(timestamp2, int):
        raise ValueError('Both timestamps must be integers.')
    if timestamp1 < 0 or timestamp2 < 0:
        raise ValueError('Timestamps cannot be negative.')

def calculate_time_difference(timestamp1, timestamp2):
    validate_timestamps(timestamp1, timestamp2)
    if timestamp2 > timestamp1:
        time_difference = timestamp2 - timestamp1
    else:
        time_difference = timestamp1 - timestamp2
    return time_difference
if __name__ == '__main__':
    ts1 = 1698043200
    ts2 = 1698129600
    difference_seconds = calculate_time_difference(ts1, ts2)
    print(f'Time Difference in seconds: {difference_seconds}')