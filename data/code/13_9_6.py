def get_circular_element(buffer, logical_index, buffer_size):
    effective_index = logical_index % buffer_size
    return buffer[effective_index]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    buffer_length = len(sample_buffer)
    index_one = 2
    index_two = 7
    index_three = 12
    result_one = get_circular_element(sample_buffer, index_one, buffer_length)
    result_two = get_circular_element(sample_buffer, index_two, buffer_length)
    result_three = get_circular_element(sample_buffer, index_three, buffer_length)
    print(result_one)
    print(result_two)
    print(result_three)