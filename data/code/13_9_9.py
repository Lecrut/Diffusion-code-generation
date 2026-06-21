def fetch_circular_buffer(buffer, logical_index):
    if not buffer:
        raise IndexError("Buffer is empty")
    size = len(buffer)
    if logical_index < -size or logical_index >= size:
        raise IndexError("Logical index out of range")
    return buffer[logical_index % size]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    index_0 = 0
    index_2 = 2
    index_4 = 4
    index_minus_1 = -1
    index_7 = 7
    print(fetch_circular_buffer(sample_buffer, index_0))
    print(fetch_circular_buffer(sample_buffer, index_2))
    print(fetch_circular_buffer(sample_buffer, index_4))
    print(fetch_circular_buffer(sample_buffer, index_minus_1))
    print(fetch_circular_buffer(sample_buffer, index_7))
    try:
        fetch_circular_buffer(sample_buffer, 5)
    except IndexError as e:
        print(str(e))
    try:
        fetch_circular_buffer([], 0)
    except IndexError as e:
        print(str(e))