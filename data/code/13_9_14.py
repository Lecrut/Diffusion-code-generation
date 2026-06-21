def fetch_circular_buffer(buffer, start_index, logical_index, capacity):
    if not buffer:
        return None
    if logical_index < 0:
        return None
    if logical_index >= len(buffer):
        return None
    
    total_elements = min(len(buffer), capacity)
    if total_elements == 0:
        return None
    
    actual_index = (start_index + logical_index) % total_elements
    return buffer[actual_index]

if __name__ == '__main__':
    buffer = [10, 20, 30, 40, 50]
    start_index = 3
    logical_index = 2
    capacity = 5
    result = fetch_circular_buffer(buffer, start_index, logical_index, capacity)
    print(result)