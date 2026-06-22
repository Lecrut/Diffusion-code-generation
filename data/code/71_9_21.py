def find_middle_element(data):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(data) == 0:
        raise ValueError("Sequence must not be empty")
    n = len(data)
    index = (n - 1) // 2
    return data[index]

if __name__ == '__main__':
    odd_sequence = [11, 22, 33, 44, 55]
    even_sequence = [11, 22, 33, 44]
    print(find_middle_element(odd_sequence))
    print(find_middle_element(even_sequence))