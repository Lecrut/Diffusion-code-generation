def fetch_circular_element(buffer, logical_index):
    if not buffer:
        raise IndexError("Cannot fetch from an empty buffer")
    actual_index = logical_index % len(buffer)
    return buffer[actual_index]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    result_positive = fetch_circular_element(sample_buffer, 3)
    result_large = fetch_circular_element(sample_buffer, 12)
    result_negative = fetch_circular_element(sample_buffer, -2)
    print(result_positive)
    print(result_large)
    print(result_negative)