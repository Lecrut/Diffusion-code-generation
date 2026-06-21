def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1], sequence[length // 2])

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1, 2, 3, 4, 5, 6]))
    print(get_middle_element("hello"))
    print(get_middle_element("worlds"))
    print(get_middle_element((10, 20, 30)))
    print(get_middle_element((10, 20, 30, 40)))
    print(get_middle_element([42]))
    print(get_middle_element([1, 2]))