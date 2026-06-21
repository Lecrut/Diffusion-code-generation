def get_center_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    center_index = length // 2
    if length % 2 == 0:
        return sequence[center_index - 1]
    return sequence[center_index]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    test_tuple = ('a', 'b', 'c', 'd')
    print(get_center_element(test_list))
    print(get_center_element(test_tuple))