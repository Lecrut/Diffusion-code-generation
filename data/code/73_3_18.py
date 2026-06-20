def validate_timestamps(timestamp1, timestamp2):
    if not (isinstance(timestamp1, int) and isinstance(timestamp2, int)):
        raise ValueError("Both timestamps must be integers.")
    if timestamp1 < 0 or timestamp2 < 0:
        raise ValueError("Timestamps must be non-negative.")

def calculate_time_difference(timestamp1, timestamp2):
    validate_timestamps(timestamp1, timestamp2)
    abs_difference = abs(timestamp2 - timestamp1)
    return abs_difference

if __name__ == '__main__':
    sample_timestamp1 = 1698086400
    sample_timestamp2 = 1698172800
    print(calculate_time_difference(sample_timestamp1, sample_timestamp2))