def fetch_from_circular_buffer(buffer, logical_index):
    if len(buffer) == 0:
        return None
    effective_index = logical_index % len(buffer)
    return buffer[effective_index]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    index_to_fetch = 7
    result = fetch_from_circular_buffer(sample_buffer, index_to_fetch)
    print(result)