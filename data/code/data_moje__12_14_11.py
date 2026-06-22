def get_middle_element(sequence):
    if not hasattr(sequence, '__len__') or hasattr(sequence, 'strip') and not hasattr(sequence, '__getitem__'):
        raise TypeError("Input must be a sequence like list, tuple, or string")
    if not isinstance(sequence, (str, bytes, list, tuple, range)):
        try:
            length = len(sequence)
        except TypeError:
            raise TypeError("Input must be a sequence with a defined length")
    else:
        length = len(sequence)
    if length == 0:
        raise ValueError("Cannot retrieve middle element from an empty sequence")
    mid = length // 2
    if length % 2 == 1:
        return sequence[mid]
    else:
        return (sequence[mid - 1], sequence[mid])

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        "hello",
        "hello world",
        (10, 20, 30, 40, 50, 60),
        b"abc",
        range(7),
        range(6)
    ]
    for case in test_cases:
        print(get_middle_element(case))