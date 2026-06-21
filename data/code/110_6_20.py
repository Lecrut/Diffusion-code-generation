def sort_timestamps(timestamps):
    return sorted(timestamps)

if __name__ == '__main__':
    timestamps = [1609459200, 1609545600, 1609372800, 1609632000]
    result = sort_timestamps(timestamps)
    print(result)