def get_circular_element(buffer, index):
    size = len(buffer)
    if size == 0:
        raise ValueError("Buffer cannot be empty")
    return buffer[index % size]

if __name__ == '__main__':
    sample_buffer = [10, 20, 30, 40, 50]
    print(get_circular_element(sample_buffer, 7))
    print(get_circular_element(sample_buffer, -2))