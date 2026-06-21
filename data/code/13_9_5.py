def fetch_from_circular_buffer(buffer, logical_index):
    if not buffer:
        return None
    actual_index = logical_index % len(buffer)
    return buffer[actual_index]

if __name__ == '__main__':
    buffer = [10, 20, 30, 40, 50]
    print(fetch_from_circular_buffer(buffer, 0))
    print(fetch_from_circular_buffer(buffer, 4))
    print(fetch_from_circular_buffer(buffer, 5))
    print(fetch_from_circular_buffer(buffer, 7))
    print(fetch_from_circular_buffer(buffer, -1))
    print(fetch_from_circular_buffer(buffer, -6))
    print(fetch_from_circular_buffer([], 5))
    print(fetch_from_circular_buffer([1], 100))
    print(fetch_from_circular_buffer([1, 2], 3))
    print(fetch_from_circular_buffer([1, 2], -3))