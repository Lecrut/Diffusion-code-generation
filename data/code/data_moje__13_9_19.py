def get_circular_element(buffer, index):
    if not buffer:
        raise IndexError("Buffer is empty")
    length = len(buffer)
    return buffer[index % length]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(get_circular_element(data, 0))
    print(get_circular_element(data, 2))
    print(get_circular_element(data, 5))
    print(get_circular_element(data, 7))
    print(get_circular_element(data, -1))
    print(get_circular_element(data, -6))