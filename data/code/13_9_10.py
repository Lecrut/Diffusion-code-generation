def fetch_circular_element(buffer, logical_index):
    if not buffer:
        return None
    actual_index = logical_index % len(buffer)
    return buffer[actual_index]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    result = fetch_circular_element(sample_buffer, 7)
    print(result)