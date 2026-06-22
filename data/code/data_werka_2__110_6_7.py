def validate_timestamps(timestamps):
    if not isinstance(timestamps, (list, tuple)):
        raise ValueError("Input must be a sequence")
    for ts in timestamps:
        if not isinstance(ts, int):
            raise ValueError("All elements must be integers")
    return list(timestamps)

def sort_unix_timestamps(timestamps):
    valid_data = validate_timestamps(timestamps)
    return sorted(valid_data)

if __name__ == '__main__':
    raw_timestamps = [1609459200, 1577836800, 1625097600, 1546300800]
    sorted_timestamps = sort_unix_timestamps(raw_timestamps)
    print(sorted_timestamps)