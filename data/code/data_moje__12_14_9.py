def get_middle_element(sequence):
    if sequence is None:
        raise ValueError("Sequence cannot be None")
    if not hasattr(sequence, '__len__') or not hasattr(sequence, '__getitem__'):
        raise TypeError("Input must be a sequence type")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    return sequence[length // 2 - 1]

if __name__ == '__main__':
    test_odd = [1, 2, 3, 4, 5]
    test_even = [1, 2, 3, 4, 5, 6]
    test_string = "hello"
    test_string_even = "abcd"
    print(get_middle_element(test_odd))
    print(get_middle_element(test_even))
    print(get_middle_element(test_string))
    print(get_middle_element(test_string_even))
    try:
        get_middle_element([])
    except ValueError as e:
        print(e)
    try:
        get_middle_element(None)
    except ValueError as e:
        print(e)
    try:
        get_middle_element(123)
    except TypeError as e:
        print(e)