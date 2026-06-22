def get_circular_buffer_element(buffer, logical_index):
    n = len(buffer)
    if n == 0:
        raise IndexError("Cannot fetch from empty buffer")
    actual_index = logical_index % n
    return buffer[actual_index]

if __name__ == '__main__':
    circular_data = [10, 20, 30, 40, 50]
    index_to_fetch = 7
    result = get_circular_buffer_element(circular_data, index_to_fetch)
    print(result)
    
    negative_index = -2
    result_neg = get_circular_buffer_element(circular_data, negative_index)
    print(result_neg)
    
    large_index = 100
    result_large = get_circular_buffer_element(circular_data, large_index)
    print(result_large)