def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence is empty")
    middle_index = length // 2
    if length % 2 == 0:
        return (sequence[middle_index - 1], sequence[middle_index])
    else:
        return sequence[middle_index]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([42]))
    print(get_middle_element("hello"))
    print(get_middle_element("world"))
    print(get_middle_element((10, 20, 30, 40, 50)))
    print(get_middle_element([1, 2, 3, 4, 5, 6]))
    print(get_middle_element("ab"))