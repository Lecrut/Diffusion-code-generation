def sort_timestamps(timestamps):
    if not all(isinstance(ts, int) for ts in timestamps):
        raise ValueError("All elements in the list must be integers")
    return sorted(timestamps)

if __name__ == '__main__':
    sample_timestamps = [1633024800, 1633111200, 1632938400]
    print(sort_timestamps(sample_timestamps))