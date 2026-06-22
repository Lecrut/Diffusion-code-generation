def validate_timestamps(timestamps):
    if not isinstance(timestamps, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    for index, value in enumerate(timestamps):
        if not isinstance(value, int):
            raise ValueError(f"Element at index {index} is not an integer")
    return list(timestamps)

def sort_unix_timestamps(timestamps):
    validated_data = validate_timestamps(timestamps)
    return sorted(validated_data)

if __name__ == '__main__':
    raw_timestamps = [1700000000, 1600000000, 1800000000, 1500000000, 1650000000]
    sorted_timestamps = sort_unix_timestamps(raw_timestamps)
    print(sorted_timestamps)