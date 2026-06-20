def calculate_time_difference(timestamp1, timestamp2):
    if not isinstance(timestamp1, int) or not isinstance(timestamp2, int):
        raise ValueError('Both timestamps must be integers (Unix epoch seconds).')
    time_difference = abs(timestamp2 - timestamp1)
    return time_difference
if __name__ == '__main__':
    sample_timestamp1 = 1635782400
    sample_timestamp2 = 1635868800
    result = calculate_time_difference(sample_timestamp1, sample_timestamp2)
    print(f'Time Difference in Seconds: {result}')