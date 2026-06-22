def get_middle_element(sequence):
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError("Input must be a sequence type")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1] + sequence[length // 2]) / 2

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element("abcde"))
    print(get_middle_element("abcd"))
    print(get_middle_element((10, 20, 30)))
    print(get_middle_element((10, 20, 30, 40)))