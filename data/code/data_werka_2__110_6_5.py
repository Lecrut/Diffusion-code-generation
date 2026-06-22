from datetime import datetime

def sort_unix_timestamps(timestamps):
    if not timestamps:
        return []
    if not all(isinstance(ts, int) for ts in timestamps):
        raise ValueError("All inputs must be integers")
    return sorted(timestamps)

if __name__ == '__main__':
    raw_timestamps = [1609459200, 1577836800, 1625097600, 1546300800]
    sorted_timestamps = sort_unix_timestamps(raw_timestamps)
    print(sorted_timestamps)