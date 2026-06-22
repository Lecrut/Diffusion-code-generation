def fetch_element(buffer, size, logical_index):
    return buffer[logical_index % size]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    sample_size = 5
    sample_index = 7
    result = fetch_element(sample_buffer, sample_size, sample_index)
    print(result)