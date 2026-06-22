def get_middle_item(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    mid_index = len(sequence) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    test_tuple = ('a', 'b', 'c', 'd', 'e')
    print(get_middle_item(test_list))
    print(get_middle_item(test_tuple))