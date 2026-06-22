def get_middle_element(sequence):
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError("Input must be a sequence (list, tuple, or string)")
    if len(sequence) == 0:
        raise ValueError("Input sequence is empty")
    mid_index = len(sequence) // 2
    if len(sequence) % 2 == 1:
        return sequence[mid_index]
    else:
        return (sequence[mid_index - 1], sequence[mid_index])

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element("hello"))
    print(get_middle_element("even"))
    print(get_middle_element((10, 20, 30)))
    print(get_middle_element((1, 2)))
    try:
        get_middle_element([])
    except ValueError as e:
        print(e)
    try:
        get_middle_element(123)
    except TypeError as e:
        print(e)