def get_middle_value(data_sequence):
    if not data_sequence:
        raise ValueError("Sequence must not be empty")
    size = len(data_sequence)
    index_map = {0: size // 2 - 1, 1: size // 2}
    return data_sequence[index_map[size % 2]]

if __name__ == '__main__':
    print(get_middle_value([1, 2, 3]))
    print(get_middle_value([1, 2, 3, 4]))
    print(get_middle_value([10]))
    print(get_middle_value([1, 2]))
    print(get_middle_value([5, 10, 15, 20, 25]))
    print(get_middle_value([100, 200, 300, 400, 500, 600]))