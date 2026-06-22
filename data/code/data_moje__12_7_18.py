def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Cannot get middle element of an empty sequence")
    middle_index = length // 2
    if length % 2 == 0:
        return (sequence[middle_index - 1], sequence[middle_index])
    else:
        return sequence[middle_index]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1]))
    print(get_middle_element([1, 2]))
    print(get_middle_element("abc"))
    print(get_middle_element("abcd"))
    print(get_middle_element((10, 20, 30, 40, 50)))
    print(get_middle_element((10, 20, 30, 40)))
    print(get_middle_element([x * 2 for x in range(7)]))
    print(get_middle_element([x ** 2 for x in range(8)]))