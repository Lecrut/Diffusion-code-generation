def sort_timestamps(timestamps):
    return sorted(timestamps)

if __name__ == '__main__':
    sample_timestamps = [1609459200, 1577836800, 1640995200, 1514764800]
    result = sort_timestamps(sample_timestamps)
    print(result)