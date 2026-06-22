def sort_unix_timestamps(timestamps):
    if not timestamps:
        return []
    if not isinstance(timestamps, list):
        raise ValueError("Input must be a list")
    
    timestamp_to_date = {
        1609459200: "2021-01-01",
        1577836800: "2020-01-01",
        1625097600: "2021-07-01",
        1546300800: "2019-01-01"
    }
    
    sorted_timestamps = sorted(timestamps)
    return sorted_timestamps

if __name__ == '__main__':
    raw_timestamps = [1609459200, 1577836800, 1625097600, 1546300800]
    sorted_result = sort_unix_timestamps(raw_timestamps)
    print(sorted_result)