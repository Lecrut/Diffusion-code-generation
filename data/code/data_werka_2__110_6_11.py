def validate_timestamps(data):
    if not isinstance(data, list):
        raise ValueError("Expected a list of timestamps")
    if len(data) == 0:
        return []
    for index, value in enumerate(data):
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(f"Element at index {index} is not an integer")
    return data

def sort_unix_timestamps(timestamps):
    validated = validate_timestamps(timestamps)
    if not validated:
        return []
    return sorted(validated)

if __name__ == '__main__':
    input_data = [1609459200, 1577836800, 1625097600, 1546300800, 1700000000]
    sorted_result = sort_unix_timestamps(input_data)
    print(sorted_result)