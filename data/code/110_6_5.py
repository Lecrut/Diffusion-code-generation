def sort_timestamps(timestamps):
    if not all(isinstance(ts, int) and ts >= 0 for ts in timestamps):
        raise ValueError("All elements must be non-negative integers.")
    return sorted(timestamps)

if __name__ == '__main__':
    sample_timestamps = [1632938400, 1633024800, 1633111200]
    print(sort_timestamps(sample_timestamps))