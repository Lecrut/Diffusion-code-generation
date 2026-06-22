def sort_unix_timestamps(timestamps):
    if not isinstance(timestamps, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if not timestamps:
        return []
    for ts in timestamps:
        if not isinstance(ts, int):
            raise ValueError("All elements must be integers")
    unit_map = {"seconds": 1, "milliseconds": 1000, "microseconds": 1000000}
    scale = unit_map.get("seconds", 1)
    converted = [ts * scale for ts in timestamps]
    converted.sort()
    return [ts // scale for ts in converted]

if __name__ == '__main__':
    raw_timestamps = [1609459200, 1577836800, 1625097600, 1546300800]
    sorted_timestamps = sort_unix_timestamps(raw_timestamps)
    print(sorted_timestamps)