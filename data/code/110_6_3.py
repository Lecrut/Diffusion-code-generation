def sort_timestamps(timestamps):
    return sorted(timestamps)

if __name__ == '__main__':
    sample_timestamps = [1633024800, 1633111200, 1632938400, 1633021200]
    sorted_timestamps = sort_timestamps(sample_timestamps)
    print(sorted_timestamps)