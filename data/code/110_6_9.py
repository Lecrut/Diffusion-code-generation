def sort_timestamps(timestamps):
    return sorted(timestamps)

if __name__ == '__main__':
    timestamps = [1633024800, 1633111200, 1632938400]
    sorted_timestamps = sort_timestamps(timestamps)
    print(sorted_timestamps)