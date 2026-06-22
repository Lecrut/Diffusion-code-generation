def fetch_from_circular_buffer(buffer, index):
    if not buffer:
        raise IndexError("Cannot fetch from empty buffer")
    normalized_index = index % len(buffer)
    return buffer[normalized_index]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    index_positive = 2
    index_negative = -1
    index_large = 7
    result1 = fetch_from_circular_buffer(sample_buffer, index_positive)
    result2 = fetch_from_circular_buffer(sample_buffer, index_negative)
    result3 = fetch_from_circular_buffer(sample_buffer, index_large)
    print(result1)
    print(result2)
    print(result3)