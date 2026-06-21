def get_circular_buffer_element(buffer, size, logical_index):
    if size <= 0:
        return None
    if logical_index < 0:
        logical_index = -(-logical_index) % size
    actual_index = logical_index % size
    return buffer[actual_index]

if __name__ == '__main__':
    buffer = [10, 20, 30, 40, 50]
    size = 5
    
    print(get_circular_buffer_element(buffer, size, 2))
    print(get_circular_buffer_element(buffer, size, 7))
    print(get_circular_buffer_element(buffer, size, -1))
    print(get_circular_buffer_element(buffer, size, 0))