def get_middle_element(sequence):
    if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
        raise TypeError("Input must be a sequence")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence is empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1], sequence[length // 2])

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element("hello"))
    print(get_middle_element("abcd"))
    try:
        get_middle_element([])
    except ValueError as e:
        print(e)
    try:
        get_middle_element(123)
    except TypeError as e:
        print(e)