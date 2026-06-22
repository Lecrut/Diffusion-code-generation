def fetch_circular_element(buffer, logical_index):
    if not buffer:
        raise IndexError("Cannot fetch from an empty buffer")
    normalized_index = logical_index % len(buffer)
    return buffer[normalized_index]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    index_to_fetch = 7
    result = fetch_circular_element(sample_buffer, index_to_fetch)
    print(result)

    negative_index = -3
    negative_result = fetch_circular_element(sample_buffer, negative_index)
    print(negative_result)

    large_index = 100
    large_result = fetch_circular_element(sample_buffer, large_index)
    print(large_result)