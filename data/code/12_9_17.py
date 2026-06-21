def get_middle_item(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    length = len(sequence)
    if length % 2 == 0:
        left_middle = sequence[length // 2 - 1]
        right_middle = sequence[length // 2]
        return (left_middle, right_middle)
    else:
        middle_index = length // 2
        return sequence[middle_index]

if __name__ == '__main__':
    test_odd = [1, 2, 3, 4, 5]
    print(get_middle_item(test_odd))

    test_even = [1, 2, 3, 4]
    print(get_middle_item(test_even))

    test_single = [42]
    print(get_middle_item(test_single))

    test_two = [1, 2]
    print(get_middle_item(test_two))

    test_strings = ['a', 'b', 'c']
    print(get_middle_item(test_strings))

    test_even_strings = ['a', 'b', 'c', 'd']
    print(get_middle_item(test_even_strings))